#!/usr/bin/env python3
"""Build the strict selection: species where several people agree over time, shown next to 花叔's sticker.

Usage: k_build_select.py <species.json> <inat-obs.jsonl> <inat-taxa.json> <out_dir> <photo-check.jsonl> [eye-check.csv]

A species is included when all of these hold:
- 花叔 2.2.0 has a sticker for it (so the two can be compared);
- AviList did not change its taxon concept, and the iNaturalist taxon has the same name;
- an iNaturalist wild observation, uploaded before 2025-11-05, with a CC0, CC BY or CC BY-SA photo,
  has at least 3 accounts currently agreeing on the species, in at least 3 different months,
  and nobody currently naming another species;
- the photo's long side is at least 1200 px;
- a bird detector finds exactly one bird, spanning at least 40% of the photo (framing only, never species);
- the eye check (if given) did not reject that photo.
"""
import csv
import html
import json
import os
import re
import sys

HUASHU_COMMIT = "fc3d95816994d3497b94e1775bbff55b93fc8f69"
RAW = f"https://raw.githubusercontent.com/alchaincyf/huashu-bird-sticker/{HUASHU_COMMIT}/"
EMAIL = re.compile(r"\S+@\S+\.\S+")
MIN_LONG_FRAC = 0.4  # the bird's box must span at least 40% of the photo's width or height


def clear_bird(f):
    """One confident bird, no other bird-like detection, big enough to see."""
    return "error" not in f and f["birds_strong"] == 1 and f["birds_any"] == 1 and f["long_frac"] >= MIN_LONG_FRAC and f.get("person_frac", 0) == 0


def main():
    species = json.load(open(sys.argv[1], encoding="utf-8"))["species"]
    obs = {}
    for line in open(sys.argv[2], encoding="utf-8"):
        if line.endswith("\n"):
            r = json.loads(line)
            obs[r["id"]] = r
    taxa = json.load(open(sys.argv[3], encoding="utf-8"))
    out = sys.argv[4]
    framing = {}
    for line in open(sys.argv[5], encoding="utf-8"):
        if line.endswith("\n"):
            r = json.loads(line)
            framing[r["obs"]] = r
    rejected = {}
    if len(sys.argv) > 6 and os.path.exists(sys.argv[6]):
        rejected = {r["obs"]: r["problem"] for r in csv.DictReader(open(sys.argv[6], encoding="utf-8")) if r["verdict"] == "reject"}
    os.makedirs(out, exist_ok=True)
    rows, reasons = [], {"checked": 0}
    for s in species:
        st = s.get("sticker")
        if not st or s["id"] not in obs:
            continue
        reasons["checked"] += 1
        why = None
        if s.get("taxonConcept") != "same":
            why = "taxon_changed"
        elif taxa[s["id"]]["match"] != "exact":
            why = "name_not_exact"
        good = [c for c in obs[s["id"]]["candidates"] if c["agree"] >= 3 and c["months"] >= 3 and c["disagree"] == 0]
        big = [c for c in good if max(c.get("w") or 0, c.get("h") or 0) >= 1200]
        checked = [c for c in big if c["obs"] in framing]
        clear = [c for c in checked if clear_bird(framing[c["obs"]]) and str(c["obs"]) not in rejected]
        if not why and not good:
            why = "no_three_people_three_months"
        elif not why and not big:
            why = "photo_too_small"
        elif not why and not checked:
            why = "framing_not_checked_yet"
        elif not why and not clear:
            why = "no_single_clear_bird"
        elif not why and f"species:{s['id']}" in rejected:
            why = "eye_check_species"
        if why:
            reasons[why] = reasons.get(why, 0) + 1
            continue
        c = max(clear, key=lambda c: (c["agree"], c["months"], c["faves"], -c["obs"]))
        rows.append({"id": s["id"], "scientific_name": s["scientificName"], "chinese": s["names"].get("zh-Hans", ""), "english": s["names"].get("en", ""),
                     "order": s["taxonomy"]["order"], "family": s["taxonomy"]["family"], "people_agree": c["agree"], "id_months": c["months"], "faves": c["faves"],
                     "research_grade_records": obs[s["id"]]["total"], "photo": c["photo"], "photo_size": f'{c.get("w")}x{c.get("h")}',
                     "observation": f'https://www.inaturalist.org/observations/{c["obs"]}', "licence": c["license"].upper(),
                     "credit": EMAIL.sub("", c["credit"] or "").strip(), "huashu_sticker": RAW + st["file"], "huashu_score": st.get("reviewScore", ""),
                     "huashu_meets_bar": "yes" if st.get("meetsQualityBar") else "no", "huashu_reference_licence": (st.get("reference") or {}).get("license") or "Not recorded"})
    fields = list(rows[0])
    with open(f"{out}/picks.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    huashu_total = sum(1 for s in species if s.get("sticker"))
    stats = {"selected": len(rows), "huashu_stickers": huashu_total, "fetched_species": len(obs), "reasons": reasons,
             "huashu_below_bar_in_selection": sum(r["huashu_meets_bar"] == "no" for r in rows),
             "median_agree": sorted(r["people_agree"] for r in rows)[len(rows) // 2], "median_months": sorted(r["id_months"] for r in rows)[len(rows) // 2]}
    json.dump(stats, open(f"{out}/stats.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    data = json.dumps([[r["id"], r["chinese"], r["english"], r["scientific_name"], r["family"], r["people_agree"], r["id_months"], r["photo"], r["observation"], r["licence"],
                        r["credit"][:120], r["huashu_sticker"], r["huashu_score"], r["huashu_meets_bar"]] for r in rows], ensure_ascii=False).replace("</", "<\\/")
    page = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "k_select_template.html"), encoding="utf-8").read()
    page = page.replace("__DATA__", data).replace("__STATS__", json.dumps(stats, ensure_ascii=False))
    open(f"{out}/index.html", "w", encoding="utf-8").write(page)
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == "__main__":
    main()
