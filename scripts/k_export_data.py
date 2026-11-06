#!/usr/bin/env python3
"""Export the selection as a dataset with the same layout and field standard as huashu-bird-sticker's data/.

Usage: k_export_data.py <picks.csv> <inat-obs.jsonl> <photo-check-v2.jsonl> <huashu data dir> <huashu commit> <out data dir> <inat-taxa.json>

<huashu data dir> holds species.json, names.csv, languages.json and field-guide.zh-Hans.json from
https://github.com/alchaincyf/huashu-bird-sticker at <huashu commit>. Every field we take from there is
copied unchanged; we replace `sticker` with our own `photo`, `evidence` and `checks`, and keep a
`huashu` block so the two can be compared.

Writes species.json, species.csv, names.csv, languages.json, field-guide.zh-Hans.json and coverage.json.
"""
import csv
import json
import os
import re
import sys

KEEP = ["id", "scientificName", "authority", "taxonomy", "names", "otherEnglishNames", "ids", "range", "subspecies",
        "extinctionStatus", "traits", "size", "conservation", "zh", "taxonConcept", "previous", "dataNotes"]
LICENSE_URL = {"CC0": "https://creativecommons.org/publicdomain/zero/1.0/", "CC BY": "https://creativecommons.org/licenses/by/4.0/",
               "CC BY-SA": "https://creativecommons.org/licenses/by-sa/4.0/"}


def clean_credit(c):
    c = re.sub(r"^\(c\)\s*", "", c or "").strip()
    c = re.sub(r",?\s*(some|no|all) rights reserved.*$", "", c, flags=re.I).strip()
    return re.sub(r"\s*\((CC[^)]*|public domain)\)$", "", c, flags=re.I).strip()


def main():
    picks_csv, obs_jsonl, framing_jsonl, hdir, commit, out, taxa_json = sys.argv[1:8]
    taxa = json.load(open(taxa_json, encoding="utf-8"))
    picks = list(csv.DictReader(open(picks_csv, encoding="utf-8")))
    cand = {}
    for line in open(obs_jsonl, encoding="utf-8"):
        if line.endswith("\n"):
            for c in json.loads(line)["candidates"]:
                cand[c["obs"]] = c
    framing = {}
    for line in open(framing_jsonl, encoding="utf-8"):
        if line.endswith("\n"):
            r = json.loads(line)
            framing[r["obs"]] = r
    hs = json.load(open(os.path.join(hdir, "species.json"), encoding="utf-8"))
    by_id = {s["id"]: s for s in hs["species"]}
    guide = json.load(open(os.path.join(hdir, "field-guide.zh-Hans.json"), encoding="utf-8"))
    raw = f"https://raw.githubusercontent.com/alchaincyf/huashu-bird-sticker/{commit}/"
    order = {s["id"]: i for i, s in enumerate(hs["species"])}
    records = []
    for p in sorted(picks, key=lambda p: order.get(p["id"], 1e9)):
        s = by_id[p["id"]]
        obs_id = int(p["observation"].rsplit("/", 1)[1])
        c, f = cand[obs_id], framing[obs_id]
        photo_id = int(re.search(r"/photos/(\d+)/", p["photo"]).group(1))
        lic = p["licence"].replace("CC-BY-SA", "CC BY-SA").replace("CC-BY", "CC BY")
        rec = {k: s[k] for k in KEEP if k in s}
        rec["ids"] = dict(rec.get("ids") or {})
        tx = taxa.get(p["id"]) or {}
        if not rec["ids"].get("inaturalist") and tx.get("match") == "exact":
            rec["ids"]["inaturalist"] = tx["taxon_id"]  # filled by this project: exact name match on iNaturalist
            rec["ids"]["inaturalistSource"] = "bird-human-picks"
        rec["photo"] = {
            "source": "iNaturalist",
            "observation": p["observation"], "observationId": obs_id,
            "page": f"https://www.inaturalist.org/photos/{photo_id}", "photoId": photo_id,
            "url": re.sub(r"/medium\.", "/original.", p["photo"]), "urlLarge": re.sub(r"/medium\.", "/large.", p["photo"]),
            "width": c.get("w"), "height": c.get("h"),
            "author": clean_credit(p["credit"]) or None, "authorUrl": f"https://www.inaturalist.org/people/{c['observer']}" if c.get("observer") else None,
            "attribution": p["credit"],
            "license": lic, "licenseUrl": LICENSE_URL.get(lic),
        }
        rec["evidence"] = {
            "agreeingIdentifiers": int(p["people_agree"]), "identificationMonths": int(p["id_months"]),
            "dissentingIdentifiers": c["disagree"], "faves": int(p["faves"]),
            "qualityGrade": "research", "captive": False, "uploadedBefore": "2025-11-05",
            "researchGradeObservationsOfSpecies": int(p["research_grade_records"]),
        }
        rec["checks"] = {
            "framing": {"model": "YOLOv10s (onnx-community/yolov10s)", "birds": f["birds_any"], "confidentBirds": f["birds_strong"],
                        "birdLongSideFraction": round(f["long_frac"], 3), "personVisible": f.get("person_frac", 0) > 0},
            "eyeCheck": "passed",
            "speciesDecidedBy": "iNaturalist identifiers; models and the eye check never decide the species",
        }
        st = s.get("sticker") or {}
        rec["huashu"] = {"commit": commit, "sticker": raw + st["file"] if st.get("file") else None,
                         "kind": st.get("kind"), "reviewScore": st.get("reviewScore"), "meetsQualityBar": st.get("meetsQualityBar")}
        records.append(rec)
    os.makedirs(out, exist_ok=True)
    meta = {"version": "0.2.0", "taxonomy": hs.get("taxonomy"), "huashuData": {"version": hs.get("version"), "commit": commit},
            "count": len(records), "species": records}
    json.dump(meta, open(os.path.join(out, "species.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    cols = ["id", "scientificName", "authority", "seq", "order", "family", "familyEnglish", "genus", "en", "zh-Hans",
            "ebird", "avibase", "wikidata", "gbif", "inaturalist", "iucn", "taxonConcept",
            "photoPage", "photoUrl", "photoWidth", "photoHeight", "photoAuthor", "photoLicense", "observation",
            "agreeingIdentifiers", "identificationMonths", "faves", "huashuSticker", "huashuReviewScore", "huashuMeetsQualityBar"]
    with open(os.path.join(out, "species.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in records:
            t, ids, ph, ev, hu = r["taxonomy"], r.get("ids") or {}, r["photo"], r["evidence"], r["huashu"]
            w.writerow([r["id"], r["scientificName"], r.get("authority", ""), t.get("seq"), t.get("order"), t.get("family"), t.get("familyEnglish"), t.get("genus"),
                        r["names"].get("en", ""), r["names"].get("zh-Hans", ""), ids.get("ebird", ""), ids.get("avibase", ""), ids.get("wikidata", ""),
                        ids.get("gbif", ""), ids.get("inaturalist", ""), (r.get("conservation") or {}).get("iucn", ""), r.get("taxonConcept", ""),
                        ph["page"], ph["url"], ph["width"], ph["height"], ph["author"] or "", ph["license"], ph["observation"],
                        ev["agreeingIdentifiers"], ev["identificationMonths"], ev["faves"], hu["sticker"] or "", hu["reviewScore"], hu["meetsQualityBar"]])

    keep = {r["id"] for r in records}
    with open(os.path.join(hdir, "names.csv"), encoding="utf-8") as src, open(os.path.join(out, "names.csv"), "w", encoding="utf-8", newline="") as dst:
        rd = csv.reader(src)
        w = csv.writer(dst)
        head = next(rd)
        w.writerow(head)
        for row in rd:
            if row and row[0] in keep:
                w.writerow(row)
    with open(os.path.join(hdir, "languages.json"), encoding="utf-8") as src:
        open(os.path.join(out, "languages.json"), "w", encoding="utf-8").write(src.read())
    g = {k: v for k, v in guide["species"].items() if k in keep}
    json.dump({"license": guide.get("license"), "note": guide.get("note"), "source": f"huashu-bird-sticker {commit}", "count": len(g), "species": g},
              open(os.path.join(out, "field-guide.zh-Hans.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    def has(path):
        n = 0
        for r in records:
            v = r
            for k in path.split("."):
                v = v.get(k) if isinstance(v, dict) else None
            n += v not in (None, "", [], {})
        return n
    fields = ["id", "scientificName", "authority", "taxonomy", "names.en", "names.zh-Hans", "otherEnglishNames", "ids.ebird", "ids.avibase",
              "ids.wikidata", "ids.gbif", "ids.inaturalist", "range.text", "range.ioc", "range.zh-Hans", "subspecies", "extinctionStatus",
              "traits", "size", "conservation.iucn", "zh", "taxonConcept", "previous", "dataNotes",
              "photo.page", "photo.url", "photo.width", "photo.height", "photo.author", "photo.authorUrl", "photo.license", "photo.licenseUrl", "photo.observation",
              "evidence.agreeingIdentifiers", "evidence.identificationMonths", "evidence.faves", "checks.framing", "checks.eyeCheck",
              "huashu.sticker", "huashu.reviewScore"]
    cov = {"count": len(records), "fields": {k: has(k) for k in fields}, "fieldGuide": len(g),
           "nameLanguages": {lang: sum(1 for r in records if r["names"].get(lang)) for lang in sorted({l for r in records for l in r["names"]})}}
    json.dump(cov, open(os.path.join(out, "coverage.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: cov["fields"][k] for k in fields}, ensure_ascii=False))


if __name__ == "__main__":
    main()
