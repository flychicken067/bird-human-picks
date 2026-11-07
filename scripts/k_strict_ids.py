#!/usr/bin/env python3
"""Recount identifications under the strict rule for a list of iNaturalist observations.

Usage: k_strict_ids.py <obs-ids.json> <inat-obs.jsonl> <out strict-ids.jsonl>

Strict rule (RULES.md, 2026-11-07): count only current identifications of the observation's species
(or a subspecies) that were made by someone other than the person who posted the observation,
and not made by accepting iNaturalist's computer-vision suggestion (identification.vision == true).
Writes one row per observation: {obs, agree_strict, months_strict, disagree, agree_all, vision_ids, own_id}.
Resumable; about one request per 200 observations, at most one request every 1.2 s.
"""
import json
import os
import ssl
import sys
import time
import urllib.request

UA = {"User-Agent": "bird-human-picks-pilot/0.3 (research prototype)"}
ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE", "/etc/ssl/cert.pem"))


def species_of(obs_jsonl):
    """obs id -> scientific name of the species it was collected for."""
    names = {}
    for line in open(obs_jsonl, encoding="utf-8"):
        if line.endswith("\n"):
            r = json.loads(line)
            for c in r["candidates"]:
                names[c["obs"]] = r["id"].replace("_", " ")
    return names


def count(o, name):
    observer = (o.get("user") or {}).get("id")
    agree_all, strict, months, disagree, vision, own = set(), set(), set(), set(), 0, False
    for i in o.get("identifications") or []:
        if not i.get("current"):
            continue
        t = i.get("taxon") or {}
        uid = (i.get("user") or {}).get("id")
        if t.get("name") == name or (t.get("name") or "").startswith(name + " "):
            agree_all.add(uid)
            vision += bool(i.get("vision"))
            own = own or uid == observer
            if uid != observer and not i.get("vision"):
                strict.add(uid)
                months.add((i.get("created_at") or "")[:7])
        elif t.get("rank") in ("species", "subspecies", "hybrid"):
            disagree.add(uid)
    return {"obs": o["id"], "agree_strict": len(strict), "months_strict": len(months - {""}), "disagree": len(disagree),
            "agree_all": len(agree_all), "vision_ids": vision, "own_id": own}


def main():
    todo = json.load(open(sys.argv[1]))
    names = species_of(sys.argv[2])
    out = sys.argv[3]
    done = set()
    if os.path.exists(out):
        done = {json.loads(l)["obs"] for l in open(out) if l.endswith("\n")}
    todo = [i for i in todo if i not in done]
    print(len(done), "done,", len(todo), "to go", flush=True)
    with open(out, "a") as fh:
        for k in range(0, len(todo), 200):
            ids = todo[k:k + 200]
            url = "https://api.inaturalist.org/v1/observations?per_page=200&id=" + ",".join(map(str, ids))
            for attempt in range(5):
                try:
                    data = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90, context=ctx))
                    break
                except Exception as e:
                    print("retry", attempt, e, flush=True)
                    time.sleep(10 * (attempt + 1))
            else:
                raise SystemExit("iNaturalist kept failing")
            for o in data["results"]:
                fh.write(json.dumps(count(o, names[o["id"]])) + "\n")
            fh.flush()
            print(k + len(ids), "/", len(todo), flush=True)
            time.sleep(1.2)


if __name__ == "__main__":
    main()
