#!/usr/bin/env python3
"""Append eye-check rejections for a replacement sheet, then write the next replacement sheet.

Usage: k_eye_record.py <picks.csv> <order.txt> <eye-check.csv> <rejections.json>
<order.txt> lists the species ids in the order the last sheet showed them (1-based numbers).
<rejections.json> maps sheet number -> reason.
"""
import csv
import json
import sys

picks = {r["id"]: r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"))}
order = open(sys.argv[2], encoding="utf-8").read().split()
rej = json.load(open(sys.argv[4], encoding="utf-8"))
with open(sys.argv[3], "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for n, why in sorted(rej.items(), key=lambda x: int(x[0])):
        r = picks[order[int(n) - 1]]
        w.writerow([r["observation"].rsplit("/", 1)[1], r["scientific_name"], "reject", why])
print(len(rej), "rejected of", len(order))
