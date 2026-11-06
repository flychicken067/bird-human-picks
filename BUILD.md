# 构建与重建 · Build

## 文件

| 路径 | 内容 |
|---|---|
| `data/` | 数据集，字段标准与花叔的 `data/` 一致，说明见 [data/README.md](data/README.md) |
| `docs/` | 网站（`site/build_site.py` 生成，15 种语言） |
| `docs/picks.csv` | 入选清单（选图脚本的直接输出） |
| `docs/eye-check.csv` | 逐张看图的排除记录 |
| `docs/review-sheet.csv` | 随机抽的 200 种盲评表，愿意的话可以填好交回 |
| `previews/` | README 画廊图和每张图的摄影师（`scripts/k_previews.py` 生成） |
| `ios/` | 离线 iOS App，见 [ios/README.md](ios/README.md) |
| `parity.json`、`PARITY.md` | 对标花叔的检查清单和最新结果，用 [ivan-parity](https://github.com/flychicken067/ivan-parity) 检查 |
| `models/` | 检测模型的来源和校验值（不含权重） |
| `RULES.md` | 选图规则和改动记录 |

## 从头生成

需要 Python 3、Pillow、numpy、onnxruntime，以及 `gh`（已登录）。

检测模型权重是 AGPL-3.0，不在本仓库。从 Hugging Face 的 `onnx-community/yolov10s`（revision 见 `models/detector-small-provenance.json`）下载 `onnx/model.onnx`，存为 `models/yolov10s-onnx-model.onnx`，脚本会校验 sha256。

```sh
python3 scripts/k_fetch_inat.py <species.json> work work/priority.json
python3 scripts/k_photo_check.py <species.json> work/inat-obs.jsonl work/inat-taxa.json work
python3 scripts/k_build_select.py <species.json> work/inat-obs.jsonl work/inat-taxa.json work/select work/photo-check-v2.jsonl docs/eye-check.csv
```

采集脚本按 iNaturalist 的建议限速：每次请求间隔约 1 秒，每 24 小时不超过 8,000 次。

## 跟随花叔的最新数据重建

```sh
scripts/rebuild_all.sh <项目目录>      # 网站、data/、App 资源
python3 scripts/k_previews.py data/species.json <照片缓存> previews
python3 scripts/k_readme.py            # 11 种语言的 README
python3 <ivan-parity>/scripts/parity_check.py parity.json --out PARITY.md
```
