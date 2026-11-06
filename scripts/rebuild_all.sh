#!/bin/bash
# Rebuild everything against huashu-bird-sticker's latest data.
# Usage: scripts/rebuild_all.sh <project dir holding work/k and 精选版/>   (run from the repo root)
set -eo pipefail
trap 'echo "rebuild_all.sh failed at line $LINENO" >&2' ERR
W="$1"
SHA=$(gh api "repos/alchaincyf/huashu-bird-sticker/commits?path=data/species.json&per_page=1" --jq '.[0].sha[0:7]')
H="$W/work/huashu-latest"
mkdir -p "$H"
for f in species.json field-guide.zh-Hans.json names.csv languages.json; do
  curl -sf -o "$H/$f" "https://raw.githubusercontent.com/alchaincyf/huashu-bird-sticker/$SHA/data/$f"
done
P="$W/精选版/picks.csv"
python3 -P site/build_site.py "$P" "$W/精选版/eye-check.csv" "$H/species.json" "$H/field-guide.zh-Hans.json" "$SHA" docs "$W/work/k/photos"
cp "$P" docs/picks.csv
python3 -I scripts/k_export_data.py "$P" "$W/work/k/inat-obs.jsonl" "$W/work/k/photo-check-v2.jsonl" "$H" "$SHA" data "$W/work/k/inat-taxa.json" >/dev/null
python3 -I scripts/k_data_readme.py data
python3 -P ios/scripts/make_bundle.py "$P" "$W/work/k/photos" ios/Resources "$H/species.json" "$H/field-guide.zh-Hans.json"
echo "rebuilt against huashu-bird-sticker $SHA"
