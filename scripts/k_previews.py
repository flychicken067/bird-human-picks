#!/usr/bin/env python3
"""Draw the README gallery: a header from CC0 photos, one plate per bird group, one bird per order.

Usage: k_previews.py <data/species.json> <photo cache dir> <out previews dir>

The photo cache holds iNaturalist medium photos named sha1(medium photo URL).jpg.
Writes JPEG plates and previews/credits.json (who took each photo in each plate, in reading order),
which the README generator prints under each plate.
"""
import hashlib
import json
import os
import sys

from PIL import Image, ImageOps

GROUPS = [  # key, families
    ("trochilidae", ["Trochilidae"]),
    ("colourful", ["Alcedinidae", "Meropidae", "Coraciidae", "Ramphastidae", "Megalaimidae", "Psittacidae", "Psittaculidae", "Cacatuidae", "Thraupidae", "Nectariniidae", "Paradisaeidae", "Pipridae"]),
    ("columbidae", ["Columbidae"]),
    ("anatidae", ["Anatidae"]),
    ("phasianidae", ["Phasianidae", "Odontophoridae", "Numididae", "Megapodiidae", "Cracidae"]),
    ("owls", ["Strigidae", "Tytonidae"]),
    ("raptors", ["Accipitridae", "Falconidae", "Pandionidae", "Cathartidae"]),
    ("herons", ["Ardeidae", "Threskiornithidae", "Ciconiidae"]),
    ("shorebirds", ["Scolopacidae", "Charadriidae", "Laridae", "Recurvirostridae", "Haematopodidae"]),
    ("songbirds", ["Muscicapidae", "Turdidae", "Parulidae", "Tyrannidae", "Icteridae", "Corvidae", "Paridae", "Fringillidae", "Estrildidae"]),
]
TILE, GAP = 300, 6


def photo(cache, s):
    medium = s["photo"]["urlLarge"].replace("/large.", "/medium.")
    p = os.path.join(cache, hashlib.sha1(medium.encode()).hexdigest() + ".jpg")
    return p if os.path.exists(p) else None


def tile(path):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    w, h = im.size
    side = min(w, h)
    return im.crop(((w - side) // 2, (h - side) // 2, (w + side) // 2, (h + side) // 2)).resize((TILE, TILE), Image.Resampling.LANCZOS)


def plate(items, cols, cache, out):
    rows = (len(items) + cols - 1) // cols
    im = Image.new("RGB", (cols * TILE + (cols + 1) * GAP, rows * TILE + (rows + 1) * GAP), (247, 246, 241))
    for i, s in enumerate(items):
        im.paste(tile(photo(cache, s)), (GAP + (i % cols) * (TILE + GAP), GAP + (i // cols) * (TILE + GAP)))
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)


def pick(pool, n):
    """Best-evidenced first, one per genus before repeating a genus."""
    pool = sorted(pool, key=lambda s: (-s["evidence"]["agreeingIdentifiers"], -s["evidence"]["faves"], s["id"]))
    seen, first, rest = set(), [], []
    for s in pool:
        (rest if s["taxonomy"]["genus"] in seen else first).append(s)
        seen.add(s["taxonomy"]["genus"])
    return (first + rest)[:n]


def credit(s):
    ph = s["photo"]
    return {"id": s["id"], "scientificName": s["scientificName"], "en": s["names"].get("en"), "zh": s["names"].get("zh-Hans"),
            "author": ph["author"] or "iNaturalist", "license": ph["license"], "page": ph["page"]}


def main():
    data = json.load(open(sys.argv[1], encoding="utf-8"))["species"]
    cache, out = sys.argv[2], sys.argv[3]
    os.makedirs(os.path.join(out, "families"), exist_ok=True)
    data = [s for s in data if photo(cache, s)]
    credits = {"groups": {}}
    for key, fams in GROUPS:
        pool = [s for s in data if s["taxonomy"]["family"] in fams]
        items = pick(pool, 12)
        plate(items, 4, cache, os.path.join(out, "families", key + ".jpg"))
        credits["groups"][key] = {"families": fams, "species": len(pool), "photos": [credit(s) for s in items]}
    orders = []
    for o in sorted({s["taxonomy"]["order"] for s in data}, key=lambda o: min(s["taxonomy"]["seq"] for s in data if s["taxonomy"]["order"] == o)):
        orders += pick([s for s in data if s["taxonomy"]["order"] == o], 1)
    plate(orders, 8, cache, os.path.join(out, "orders.jpg"))
    credits["orders"] = [credit(s) for s in orders]
    cc0 = [s for s in data if s["photo"]["license"] == "CC0"]
    seen, header = set(), []
    for s in sorted(cc0, key=lambda s: (-s["evidence"]["agreeingIdentifiers"], s["id"])):
        if s["taxonomy"]["order"] not in seen:
            header.append(s)
            seen.add(s["taxonomy"]["order"])
        if len(header) == 8:
            break
    plate(header, 8, cache, os.path.join(out, "header.jpg"))
    credits["header"] = [credit(s) for s in header]
    json.dump(credits, open(os.path.join(out, "credits.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print({k: v["species"] for k, v in credits["groups"].items()}, "orders", len(orders), "header", len(header))


if __name__ == "__main__":
    main()
