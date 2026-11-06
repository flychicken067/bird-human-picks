#!/usr/bin/env python3
"""Collect bird photos that the Wikimedia Commons community has voted on.

Usage: k_fetch_commons_votes.py <species.json> <out.jsonl>

Three community labels, each decided by people, not by this script:
- FP  Featured picture: promoted by a community vote.
- VI  Valued image: reviewed as the most useful image of its subject (the species).
- QI  Quality image: passed a technical-quality review by another user.

For every species in 花叔 2.2.0 the script looks in two places:
1. Commons' own per-species categories, e.g. "Quality images of Erithacus rubecula";
2. files that are directly in the species category and also in "Quality images" or
   "Featured pictures on Wikimedia Commons".
For each file found it records the labels, licence, author, size and an 800 px thumbnail.
One row per species: {id, files: [...]}. Resumable: species already in <out.jsonl> are skipped.
"""
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "bird-human-picks-pilot/0.3 (research prototype)"}
ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE", "/etc/ssl/cert.pem"))
LABEL_CATS = {"FP": "Featured pictures of {}", "VI": "Valued images of {}", "QI": "Quality images of {}"}
GLOBAL = {"Quality images": "QI", "Featured pictures on Wikimedia Commons": "FP"}
TAG = re.compile(r"<[^>]+>")
BATCH = 40


def get(params):
    params = {**params, "format": "json", "formatversion": "2", "maxlag": "5"}
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(6):
        try:
            time.sleep(0.5)
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60, context=ctx) as r:
                d = json.load(r)
            if "error" in d and d["error"].get("code") == "maxlag":
                time.sleep(5 * (attempt + 1))
                continue
            return d
        except Exception as e:  # network hiccup: back off and retry
            print("retry", attempt, e, file=sys.stderr, flush=True)
            time.sleep(5 * (attempt + 1))
    raise RuntimeError("Commons API kept failing")


def all_pages(params, key):
    cont = {}
    while True:
        d = get({**params, **cont})
        yield from d.get("query", {}).get(key, [])
        if "continue" not in d:
            return
        cont = d["continue"]


def file_info(titles):
    """Licence, author, size, thumbnail and categories for up to 50 files."""
    out = {}
    for i in range(0, len(titles), 50):
        d = get({"action": "query", "prop": "imageinfo|categories", "titles": "|".join(titles[i:i + 50]), "iiprop": "url|size|extmetadata",
                 "iiurlwidth": "800", "iiextmetadatafilter": "LicenseShortName|Artist", "cllimit": "max", "clshow": "!hidden"})
        for p in d["query"]["pages"]:
            ii = (p.get("imageinfo") or [{}])[0]
            meta = ii.get("extmetadata", {})
            out[p["title"]] = {"file": p["title"], "w": ii.get("width"), "h": ii.get("height"), "thumb": ii.get("thumburl"), "page": ii.get("descriptionurl"),
                               "license": meta.get("LicenseShortName", {}).get("value", ""),
                               "artist": TAG.sub("", meta.get("Artist", {}).get("value", "")).strip()[:200],
                               "cats": [c["title"][9:] for c in p.get("categories", [])]}
    return out


def main():
    species = [s for s in json.load(open(sys.argv[1], encoding="utf-8"))["species"] if s.get("sticker")]
    out_path = sys.argv[2]
    done = set()
    if os.path.exists(out_path):
        done = {json.loads(l)["id"] for l in open(out_path, encoding="utf-8") if l.endswith("\n")}
    todo = [s for s in species if s["id"] not in done]
    print(f"{len(done)} done, {len(todo)} to go", flush=True)
    with open(out_path, "a", encoding="utf-8") as out:
        for b in range(0, len(todo), BATCH):
            batch = todo[b:b + BATCH]
            found = {s["id"]: {} for s in batch}  # id -> {file title: set(labels)}
            # 1. per-species label categories
            names = {}
            for s in batch:
                for label, pat in LABEL_CATS.items():
                    names["Category:" + pat.format(s["scientificName"])] = (s["id"], label)
            titles = list(names)
            for i in range(0, len(titles), 50):
                d = get({"action": "query", "prop": "categoryinfo", "titles": "|".join(titles[i:i + 50])})
                for p in d["query"]["pages"]:
                    if p.get("categoryinfo", {}).get("files"):
                        sid, label = names[p["title"]]
                        for m in all_pages({"action": "query", "list": "categorymembers", "cmtitle": p["title"], "cmtype": "file", "cmlimit": "500"}, "categorymembers"):
                            found[sid].setdefault(m["title"], set()).add(label)
            # 2. files directly in the species category that are also QI or FP
            by_cat = {s["scientificName"]: s["id"] for s in batch}
            q = "incategory:" + "|".join(n.replace(" ", "_") for n in by_cat) + " incategory:Quality_images|Featured_pictures_on_Wikimedia_Commons"
            hits = [r["title"] for r in all_pages({"action": "query", "list": "search", "srnamespace": "6", "srlimit": "500", "srsearch": q, "srprop": ""}, "search")]
            info = file_info(sorted({t for f in found.values() for t in f} | set(hits)))
            for t in hits:
                cats = set(info.get(t, {}).get("cats", []))
                for name, sid in by_cat.items():
                    if name in cats:
                        found[sid].setdefault(t, set()).update(GLOBAL[c] for c in cats & set(GLOBAL))
            for s in batch:
                files = []
                for t, labels in found[s["id"]].items():
                    f = dict(info.get(t, {"file": t}))
                    cats = set(f.pop("cats", []))
                    labels |= {GLOBAL[c] for c in cats & set(GLOBAL)}
                    f["labels"] = sorted(labels)
                    if f.get("thumb"):
                        f["thumb"] = f["thumb"].split("?")[0]
                    if labels:  # the search index can lag; keep only labels the live categories confirm
                        files.append(f)
                out.write(json.dumps({"id": s["id"], "scientific_name": s["scientificName"], "files": files}, ensure_ascii=False) + "\n")
            out.flush()
            print(f"{len(done) + b + len(batch)} / {len(species)}", flush=True)


if __name__ == "__main__":
    main()
