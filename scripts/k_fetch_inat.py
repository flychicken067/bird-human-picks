#!/usr/bin/env python3
"""Collect human identifications from iNaturalist by exact taxon ID, for every species.

Usage: k_fetch_inat.py <species.json> <out_dir> [priority_ids.json]

1. Lists all bird species taxa in bulk (active and inactive) and maps each AviList
   scientific name to a taxon: exact active name, else an inactive name with exactly
   one current replacement (flagged "renamed"). Anything else stays unmapped.
2. For each mapped species, keeps candidate photos with permissive licences.

Resumable. Stays near 1 request a second and pauses at DAILY_BUDGET in any 24 hours.
Keeps counts and dates only: no coordinates and no identifier names.
"""
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE", "/etc/ssl/cert.pem"))
UA = {"User-Agent": "bird-human-picks-pilot/0.3 (research prototype)"}
API = "https://api.inaturalist.org/v1/"
DAILY_BUDGET = 8000
CUTOFF = "2025-11-05"
LICENCES = {"cc0", "cc-by", "cc-by-sa"}
stamps = []


def get(path, params):
    while len([t for t in stamps if t > time.time() - 86400]) >= DAILY_BUDGET:
        print("daily budget reached, waiting", flush=True)
        time.sleep(600)
    url = API + path + "?" + urllib.parse.urlencode(params)
    failures = 0
    while True:
        start = time.time()
        stamps.append(start)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120, context=ctx) as r:
                data = json.load(r)
            time.sleep(max(0, 1.1 - (time.time() - start)))
            return data
        except urllib.error.HTTPError as e:
            failures += 1
            if failures == 10:
                raise
            time.sleep(120 if e.code == 429 else 2 ** failures)
        except Exception:
            failures += 1
            if failures == 10:
                raise
            time.sleep(2 ** failures)


def list_taxa(active):
    rows, above = [], 0
    while True:
        d = get("taxa", {"taxon_id": 3, "rank": "species", "is_active": active, "per_page": 200, "order_by": "id", "order": "asc", "id_above": above})
        if not d["results"]:
            return rows
        rows += [{"id": t["id"], "name": t["name"], "obs": t.get("observations_count", 0), "syn": t.get("current_synonymous_taxon_ids") or [], "extinct": t.get("extinct", False)} for t in d["results"]]
        above = d["results"][-1]["id"]


def taxon_map(species, path):
    if os.path.exists(path):
        return json.load(open(path, encoding="utf-8"))
    active = list_taxa("true")
    inactive = list_taxa("false")
    print("taxa", len(active), len(inactive), flush=True)
    by_active = {}
    for t in active:
        by_active.setdefault(t["name"], []).append(t)
    by_old = {}
    for t in inactive:
        by_old.setdefault(t["name"], []).append(t)
    ids = {t["id"]: t for t in active}
    out = {}
    for s in species:
        sci = s["scientificName"]
        hit = by_active.get(sci, [])
        if len(hit) == 1:
            out[s["id"]] = {"taxon_id": hit[0]["id"], "inat_name": sci, "match": "exact", "obs": hit[0]["obs"]}
            continue
        old = by_old.get(sci, [])
        syn = {x for t in old for x in t["syn"]}
        if len(syn) == 1 and next(iter(syn)) in ids:
            t = ids[next(iter(syn))]
            out[s["id"]] = {"taxon_id": t["id"], "inat_name": t["name"], "match": "renamed", "obs": t["obs"]}
        else:
            out[s["id"]] = {"taxon_id": None, "inat_name": "", "match": "lumped_or_split" if len(syn) > 1 else "none", "obs": 0}
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False)
    return out


def candidate(o, name):
    photo = next((p for p in o.get("photos") or [] if p.get("license_code") in LICENCES and p.get("url")), None)
    taxon = (o.get("taxon") or {}).get("name") or ""
    if not photo or not (taxon == name or taxon.startswith(name + " ")):
        return None
    agree, months, disagree = set(), set(), set()
    strict, strict_months = set(), set()  # without the poster's own ID and without AI-suggested IDs (RULES.md, 2026-11-07)
    poster = (o.get("user") or {}).get("id")
    for i in o.get("identifications") or []:
        if not i.get("current"):
            continue
        t = i.get("taxon") or {}
        uid = (i.get("user") or {}).get("id")
        if t.get("name") == name or (t.get("name") or "").startswith(name + " "):
            agree.add(uid)
            months.add((i.get("created_at") or "")[:7])
            if uid != poster and not i.get("vision"):
                strict.add(uid)
                strict_months.add((i.get("created_at") or "")[:7])
        elif t.get("rank") in ("species", "subspecies", "hybrid"):
            disagree.add(uid)
    dims = photo.get("original_dimensions") or {}
    return {"obs": o["id"], "observer": (o.get("user") or {}).get("id"), "faves": o.get("faves_count", 0), "agree": len(agree), "months": len(months - {""}), "disagree": len(disagree),
            "agree_strict": len(strict), "months_strict": len(strict_months - {""}),
            "license": photo["license_code"], "credit": photo.get("attribution"), "photo": photo["url"].replace("/square.", "/medium."), "w": dims.get("width"), "h": dims.get("height"),
            "created": (o.get("created_at") or "")[:10], "n_photos": len(o.get("photos") or [])}


def main():
    species = json.load(open(sys.argv[1], encoding="utf-8"))["species"]
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    first = json.load(open(sys.argv[3], encoding="utf-8")) if len(sys.argv) > 3 else []
    rank = {x: i for i, x in enumerate(first)}
    species.sort(key=lambda s: (rank.get(s["id"], len(rank)), s["taxonomy"]["seq"]))
    tmap = taxon_map(species, f"{out}/inat-taxa.json")
    path = f"{out}/inat-obs.jsonl"
    done = set()
    if os.path.exists(path):
        done = {json.loads(l)["id"] for l in open(path, encoding="utf-8") if l.endswith("\n")}
    todo = [s for s in species if s["id"] not in done and tmap[s["id"]]["taxon_id"]]
    print("species to fetch", len(todo), flush=True)
    with open(path, "a", encoding="utf-8") as f:
        for n, s in enumerate(todo):
            m = tmap[s["id"]]
            d = get("observations", {"taxon_id": m["taxon_id"], "quality_grade": "research", "photos": "true", "captive": "false", "photo_license": ",".join(sorted(LICENCES)),
                                     "created_d2": CUTOFF, "order_by": "votes", "per_page": 30})
            cands = [c for c in (candidate(o, m["inat_name"]) for o in d.get("results") or []) if c]
            f.write(json.dumps({"id": s["id"], "total": d.get("total_results", 0), "candidates": cands}, ensure_ascii=False) + "\n")
            f.flush()
            if n % 250 == 0:
                print("fetched", n, flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
