#!/usr/bin/env python3
"""Turn docs/picks.csv into the app's offline bundle.

Usage: make_bundle.py <picks.csv> <photo_cache_dir> <out_dir>

The photo cache holds the iNaturalist medium photos named sha1(photo_url).jpg
(what scripts/k_photo_check.py downloads). Writes:
  <out_dir>/App/birds.json, <out_dir>/App/Photos/<id>.jpg  (long side 800 px)
  <out_dir>/Widget/birds.json, <out_dir>/Widget/Thumbs/<id>.jpg (long side 320 px)
"""
import csv, hashlib, json, os, sys, urllib.request
from PIL import Image, ImageOps

picks, cache, out = sys.argv[1:4]
rows = list(csv.DictReader(open(picks, encoding="utf-8")))
for sub in ("App/Photos", "Widget/Thumbs"):
    os.makedirs(os.path.join(out, sub), exist_ok=True)
birds, missing = [], []
for r in rows:
    src = os.path.join(cache, hashlib.sha1(r["photo"].encode()).hexdigest() + ".jpg")
    if not os.path.exists(src):  # not cached yet: download the photo listed in picks.csv
        try:
            req = urllib.request.Request(r["photo"], headers={"User-Agent": "bird-human-picks/0.1"})
            os.makedirs(cache, exist_ok=True)
            open(src, "wb").write(urllib.request.urlopen(req, timeout=60).read())
        except Exception:
            missing.append(r["id"]); continue
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    for sub, size, q in (("App/Photos", 800, 78), ("Widget/Thumbs", 320, 72)):
        t = im.copy(); t.thumbnail((size, size), Image.Resampling.LANCZOS)
        t.save(os.path.join(out, sub, r["id"] + ".jpg"), "JPEG", quality=q, optimize=True, progressive=True)
    birds.append({"id": r["id"], "zh": r["chinese"], "en": r["english"], "sci": r["scientific_name"], "order": r["order"], "family": r["family"],
                  "agree": int(r["people_agree"]), "months": int(r["id_months"]), "observation": r["observation"],
                  "licence": r["licence"], "credit": r["credit"]})
birds.sort(key=lambda b: (b["order"], b["family"], b["sci"]))
json.dump(birds, open(os.path.join(out, "App/birds.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump([{k: b[k] for k in ("id", "zh", "en", "sci", "agree", "months")} for b in birds], open(os.path.join(out, "Widget/birds.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(birds), "birds;", len(missing), "missing photos", missing[:5])
