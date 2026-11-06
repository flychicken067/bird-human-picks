#!/usr/bin/env python3
"""Draw the blind review sample: 200 selected species, both images, sources hidden.

Usage: k_review_sheet.py <picks.csv> <out_dir>
Writes review-sheet.csv (what reviewers see: two images in random order) and
review-key.csv (which image is which; keep it from reviewers).
"""
import csv
import random
import sys

rows = sorted(csv.DictReader(open(sys.argv[1], encoding="utf-8")), key=lambda r: r["id"])
rng = random.Random(20261106)
sample = rng.sample(rows, min(200, len(rows)))
with open(f"{sys.argv[2]}/review-sheet.csv", "w", encoding="utf-8", newline="") as f, open(f"{sys.argv[2]}/review-key.csv", "w", encoding="utf-8", newline="") as k:
    sheet, key = csv.writer(f), csv.writer(k)
    sheet.writerow(["item", "species_chinese", "scientific_name", "image_1", "image_2", "image_1_is_this_species(yes/no/unsure)", "image_2_is_this_species(yes/no/unsure)", "prefer(1/2/same)", "reviewer", "note"])
    key.writerow(["item", "image_1_source", "image_2_source"])
    for i, r in enumerate(sample, 1):
        pair = [("photo", r["photo"]), ("huashu", r["huashu_sticker"])]
        rng.shuffle(pair)
        sheet.writerow([i, r["chinese"], r["scientific_name"], pair[0][1], pair[1][1], "", "", "", "", ""])
        key.writerow([i, pair[0][0], pair[1][0]])
print(len(sample), "items")
