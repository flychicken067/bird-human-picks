#!/usr/bin/env python3
"""Turn docs/picks.csv into the app's offline bundle.

Usage: make_bundle.py <picks.csv> <photo_cache_dir> <out_dir> [huashu species.json] [huashu field-guide.zh-Hans.json]

The photo cache holds the iNaturalist medium photos named sha1(photo_url).jpg
(what scripts/k_photo_check.py downloads). Writes:
  <out_dir>/App/birds.json, <out_dir>/App/Photos/<id>.jpg  (long side 800 px)
  <out_dir>/Widget/birds.json, <out_dir>/Widget/Thumbs/<id>.jpg (long side 320 px)
"""
import csv, hashlib, json, os, re, sys, urllib.request
from PIL import Image, ImageOps

picks, cache, out = sys.argv[1:4]
species = {s["id"]: s for s in json.load(open(sys.argv[4], encoding="utf-8"))["species"]} if len(sys.argv) > 4 else {}
guide = json.load(open(sys.argv[5], encoding="utf-8"))["species"] if len(sys.argv) > 5 else {}


def clean_credit(c):
    c = re.sub(r"^\(c\)\s*", "", c or "").strip()
    c = re.sub(r",?\s*(some|no|all) rights reserved.*$", "", c, flags=re.I).strip()
    return re.sub(r"\s*\((CC[^)]*|public domain)\)$", "", c, flags=re.I).strip() or "iNaturalist"


def mass(g):
    if not g:
        return None
    return f"{g / 1000:.3g} kg" if g >= 1000 else f"{g:.3g} g"


def span(v, unit):
    if not v:
        return None
    lo, hi = v
    return f"{lo:g}–{hi:g} {unit}" if hi and hi != lo else f"{lo:g} {unit}"
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
    sp = species.get(r["id"], {})
    zh, size, traits, g = sp.get("zh") or {}, sp.get("size") or {}, sp.get("traits") or {}, guide.get(r["id"]) or {}
    b = {"id": r["id"], "zh": r["chinese"], "en": r["english"], "sci": r["scientific_name"], "order": r["order"], "family": r["family"],
         "agree": int(r["people_agree"]), "months": int(r["id_months"]), "observation": r["observation"],
         "licence": r["licence"].replace("CC-BY-SA", "CC BY-SA").replace("CC-BY", "CC BY"), "credit": clean_credit(r["credit"]),
         "zhOrder": zh.get("order"), "zhFamily": zh.get("family"), "length": span(size.get("bodyLengthCm"), "cm"),
         "wingspan": span(size.get("wingspanCm"), "cm"), "weight": mass(traits.get("massG")),
         "iucn": ((sp.get("conservation") or {}).get("iucn") or "").split(" ")[0] or None,
         "range": (sp.get("range") or {}).get("zh-Hans") or (sp.get("range") or {}).get("text"),
         "impression": g.get("impression"), "marks": g.get("marks")}
    birds.append({k: v for k, v in b.items() if k in ("zh", "en") or v not in (None, "", [])})
# keep the order of picks.csv, which follows the taxonomic sequence
json.dump(birds, open(os.path.join(out, "App/birds.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump([{k: b[k] for k in ("id", "zh", "en", "sci", "agree", "months")} for b in birds], open(os.path.join(out, "Widget/birds.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(birds), "birds;", len(missing), "missing photos", missing[:5])
