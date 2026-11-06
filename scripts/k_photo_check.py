#!/usr/bin/env python3
"""Check the framing of candidate photos: is there exactly one clearly visible bird?

Usage: k_photo_check.py <species.json> <inat-obs.jsonl> <inat-taxa.json> <work_dir>

For each species whose iNaturalist evidence meets the strict rule (3 people, 3 months,
no other species named, long side >= 1200 px), up to MAX_PER_SPECIES candidates are
downloaded at medium size and passed to a COCO object detector (YOLOv10s, AGPL-3.0,
weights in models/). The detector only answers "where are the birds"; it never
decides the species. Results go to <work_dir>/photo-check.jsonl. Resumable.
"""
import concurrent.futures as cf
import hashlib
import importlib.util
import io
import json
import os
import ssl
import sys
import time
import urllib.request

from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("bird_detector", os.path.join(ROOT, "scripts", "bird_detector.py"))
bird_detector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bird_detector)

ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE", "/etc/ssl/cert.pem"))
UA = {"User-Agent": "bird-human-picks-pilot/0.3 (research prototype)"}
MAX_PER_SPECIES = 6


def strict(c):
    return c["agree"] >= 3 and c["months"] >= 3 and c["disagree"] == 0 and max(c.get("w") or 0, c.get("h") or 0) >= 1200


def fetch(url, path):
    if os.path.exists(path):
        return open(path, "rb").read()
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60, context=ctx) as r:
                data = r.read()
            with open(path, "wb") as f:
                f.write(data)
            return data
        except Exception:
            time.sleep(2 ** attempt)
    return None


def detect_people(det, im):
    """Same preprocessing as BirdDetector.detect, but for the COCO person class (a hand or a holder)."""
    import numpy as np
    w, h = im.size
    scale = 640 / max(w, h)
    nw, nh = round(w * scale), round(h * scale)
    canvas = Image.new("RGB", (640, 640))
    canvas.paste(im.resize((nw, nh), Image.Resampling.BILINEAR), (0, 0))
    inp = np.asarray(canvas, dtype=np.float32).transpose(2, 0, 1)[None] / 255
    rows = det.session.run(None, {det.input: inp})[0].reshape(-1, 6)
    best = 0.0
    for x1, y1, x2, y2, score, label in rows:
        if int(label) == 0 and score >= 0.3:
            best = max(best, (min(w, x2 * w / nw) - max(0, x1 * w / nw)) * (min(h, y2 * h / nh) - max(0, y1 * h / nh)) / (w * h))
    return round(float(best), 4)


def measure(det, data):
    im = ImageOps.exif_transpose(Image.open(io.BytesIO(data))).convert("RGB")
    w, h = im.size
    boxes = det.detect(im)
    strong = [b for b in boxes if b["score"] >= 0.5]
    out = {"img_w": w, "img_h": h, "birds_any": len(boxes), "birds_strong": len(strong), "person_frac": detect_people(det, im)}
    if len(strong) == 1:
        x1, y1, x2, y2 = strong[0]["box"]
        out["area_frac"] = round((x2 - x1) * (y2 - y1) / (w * h), 4)
        out["long_frac"] = round(max((x2 - x1) / w, (y2 - y1) / h), 4)
        out["score"] = strong[0]["score"]
    return out


def main():
    species = json.load(open(sys.argv[1], encoding="utf-8"))["species"]
    taxa = json.load(open(sys.argv[3], encoding="utf-8"))
    work = sys.argv[4]
    photos = os.path.join(work, "photos")
    os.makedirs(photos, exist_ok=True)
    ok_species = {s["id"] for s in species if s.get("sticker") and s.get("taxonConcept") == "same" and taxa[s["id"]]["match"] == "exact"}
    jobs = []
    for line in open(sys.argv[2], encoding="utf-8"):
        if not line.endswith("\n"):
            continue
        r = json.loads(line)
        if r["id"] not in ok_species:
            continue
        cands = sorted((c for c in r["candidates"] if strict(c)), key=lambda c: (-c["agree"], -c["months"], -c["faves"], c["obs"]))
        jobs += [(r["id"], c) for c in cands[:MAX_PER_SPECIES]]
    path = os.path.join(work, "photo-check-v2.jsonl")  # v2 adds person_frac
    done = set()
    if os.path.exists(path):
        done = {json.loads(l)["obs"] for l in open(path, encoding="utf-8") if l.endswith("\n")}
    jobs = [j for j in jobs if j[1]["obs"] not in done]
    print("photos to check", len(jobs), flush=True)
    det = bird_detector.BirdDetector("small")
    with open(path, "a", encoding="utf-8") as f, cf.ThreadPoolExecutor(4) as pool:
        for start in range(0, len(jobs), 40):
            part = jobs[start:start + 40]
            futures = [pool.submit(fetch, c["photo"], os.path.join(photos, hashlib.sha1(c["photo"].encode()).hexdigest() + ".jpg")) for _, c in part]
            for (sid, c), fut in zip(part, futures):
                data = fut.result()
                row = {"id": sid, "obs": c["obs"]}
                if data is None:
                    row["error"] = "download_failed"
                else:
                    try:
                        row.update(measure(det, data))
                    except Exception as e:
                        row["error"] = type(e).__name__
                f.write(json.dumps(row) + "\n")
            f.flush()
            if start % 1000 == 0:
                print("checked", start, flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
