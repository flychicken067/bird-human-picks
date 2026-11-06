# Notice

This repository links to, but does not contain, material from these sources.

**Bird photographs.** From iNaturalist observations. Each photograph remains the copyright of its photographer and is used under the licence listed for it in `docs/picks.csv` (CC0, CC BY or CC BY-SA). The credit line for each photo is in the same file and is shown under the photo on the page.

**Stickers.** "Bird stickers: huashu-bird-sticker by Huashu, CC BY 4.0", https://github.com/alchaincyf/huashu-bird-sticker, commit fc3d95816994d3497b94e1775bbff55b93fc8f69 (data 2.2.0). Species names and taxonomy in `docs/picks.csv` come from the same repository's `data/species.json` (MIT).

**Identifications.** Counts of agreeing identifications come from the iNaturalist API. No identifier names or observation coordinates are stored here.

**Detector.** YOLOv10s, onnx-community/yolov10s, AGPL-3.0. The weights are not included; `models/` only holds the provenance record and the model config needed to check them.

# 说明

本仓库只链接、不存放以下内容：iNaturalist 照片（版权归摄影师，授权见 `docs/picks.csv`）；花叔的贴纸（CC BY 4.0）；检测模型权重（AGPL-3.0）。不保存鉴定者姓名和观测坐标。

## huashu-bird-sticker data (MIT)

`data/` and the species pages reuse fields from huashu-bird-sticker's `data/species.json`, `names.csv`, `languages.json` and `field-guide.zh-Hans.json` (pinned commit in `data/species.json` → `huashuData`).

Those fields are MIT-licensed by Huashu (alchaincyf); the full license text, with its copyright notice, is in [LICENSES/huashu-bird-sticker-MIT.txt](LICENSES/huashu-bird-sticker-MIT.txt). Third-party parts of that data keep their own terms: AviList (CC BY 4.0), IOC World Bird List (CC BY 3.0), AVONET (CC BY 4.0), Wikidata (CC0); the Chinese field-guide notes are CC BY-SA 4.0.
