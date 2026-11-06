# 鸟类人选图鉴 · bird-human-picks

花叔的 [huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker) 给每种鸟画了一张 AI 贴纸，由 AI 打分。这个项目回答另一个问题：**如果图片由人拍、物种由人认定，能做到什么程度？**

每种鸟选一张 iNaturalist 上的野外照片，要求至少 3 个账号在至少 3 个不同月份认定它是这个物种，并且没有人给出别的物种。页面把这张照片和花叔的贴纸并排放，方便直接比较。

网站：https://flychicken067.github.io/bird-human-picks/ ，15 种语言，每种鸟一个页面（体型、保护等级、分布、各语言鸟名、引用方式、报错入口），可选和花叔贴纸并排对比。

## 现在的数字

| | |
|---|---|
| 入选鸟种 | 1,209 种（花叔有贴纸的是 10,973 种） |
| 已查询的鸟种 | 7,894 / 11,011，全量查询仍在进行，入选数会继续增加 |
| 每种鸟的鉴定 | 中位数 5 个账号，跨 3 个不同月份 |
| 照片授权 | CC BY 923 张，CC0 163 张，CC BY-SA 123 张 |
| 花叔贴纸未达他自己标准的鸟种 | 5 种（按花叔 2.2.6 数据；2.2.0 时是 55 种，他已重画了一批） |
| 和花叔的错误数比较 | 要等两版公开一段时间、积累了被人指出的错误后才能做 |

## 入选规则

1. 花叔 2.2.0 有这种鸟的贴纸，两版才能比较。
2. AviList 没有调整过这种鸟的物种划分，iNaturalist 的学名也完全一致。
3. iNaturalist 野外研究级观测，2025-11-05 之前上传。至少 3 个账号当前认定为这个物种（含亚种），认定跨至少 3 个不同月份，且没有人当前给出其他物种。
4. 照片授权为 CC0、CC BY 或 CC BY-SA，原图长边至少 1200 像素。
5. 构图检查：YOLOv10s 检测模型只找到一只鸟，鸟框至少占画面长或宽的 40%，画面里没有人或手。模型只看有几只鸟、多大，不判断物种。
6. Claude 逐张看过所有照片。被排除的照片自动换成下一张候选，换上的也逐张看过。

规则 1–4 用的是人的判断，规则 5–6 只决定这张图能不能放进图鉴，不改变物种结论。完整的预先登记规则见 [RULES.md](RULES.md)。

## 看图排除了什么

[`docs/eye-check.csv`](docs/eye-check.csv) 记录了全部 368 条排除，每条都有观测编号和原因：

| 原因 | 张数 |
|---|---|
| 鸟被遮挡、太小或模糊 | 265 |
| 只拍到头或身体的一部分 | 38 |
| 多只鸟或雏鸟 | 21 |
| 家禽、家养色型或疑似笼养 | 14 |
| 死鸟 | 13 |
| 鸟在人手上 | 7 |
| 只有羽毛或鸟巢 | 5 |
| 手绘画或翻拍屏幕 | 4 |
| 照片里是别的鸟 | 1 |

最后一类：一条安氏蜂鸟的观测，3 个人认定的是这条观测，但取到的那张照片里是一只猫头鹰。原鸡整体排除，因为候选照片大多是家鸡。

## 和花叔版比

**强在：**
- **物种依据是人。** 每种鸟都有至少 3 个人跨月认定。
- **授权清楚。** 每张照片的授权和作者都能查到，全部允许商用。

**弱在：**
- **数量少。** 目前只有花叔的 1/9。
- **风格不统一。** 真实照片的光线、姿态和背景各不相同，也不是透明贴纸。
- **还没有效果上的比较。** 3 个账号不等于 3 位专家，他们也可能跟随别人的鉴定。

这个项目只用网上已经存在的人的判断，不专门招人打分。和花叔比效果，要等两版公开一段时间后，比较各自被人指出的物种错误。在那之前，只能说这版**物种依据更强**，不能说效果更好。规则和改动记录见 [RULES.md](RULES.md)。

## 发现错误？

哪张图不是这个物种，或者画面有问题，请开 issue，写上学名和原因。这些纠错就是比较两版的依据。

[`docs/review-sheet.csv`](docs/review-sheet.csv) 随机抽了 200 种，两张图顺序打乱、不标来源。愿意的话可以填好交回，作为补充。

## 文件

| 路径 | 内容 |
|---|---|
| `docs/` | 网站（由 `site/build_site.py` 生成，15 种语言、18,165 个页面） |
| `parity.json`、`PARITY.md` | 对标花叔 birdalbum.com 的检查清单和最新检查结果，用 [ivan-parity](https://github.com/flychicken067/ivan-parity) 检查 |
| `docs/picks.csv` | 入选清单：物种、认定人数和月份、照片、观测链接、授权、作者、对应的花叔贴纸 |
| `docs/eye-check.csv` | 看图排除记录 |
| `docs/stats.json` | 每条未入选原因的计数 |
| `scripts/` | 采集、构图检查、生成页面的脚本 |
| `models/` | 检测模型的来源和校验值（不含权重） |

## 自己重新生成

需要 Python 3、Pillow、numpy、onnxruntime，以及花叔仓库的 `data/species.json`（网站还要 `data/field-guide.zh-Hans.json`）。

检测模型权重是 AGPL-3.0，没有放进本仓库。从 Hugging Face 的 `onnx-community/yolov10s`（revision 见 `models/detector-small-provenance.json`）下载 `onnx/model.onnx`，存为 `models/yolov10s-onnx-model.onnx`，脚本会校验 sha256。

```sh
python3 scripts/k_fetch_inat.py <species.json> work work/priority.json
python3 scripts/k_photo_check.py <species.json> work/inat-obs.jsonl work/inat-taxa.json work
python3 scripts/k_build_select.py <species.json> work/inat-obs.jsonl work/inat-taxa.json work/select work/photo-check-v2.jsonl docs/eye-check.csv
cp work/select/picks.csv docs/picks.csv
# 网站：花叔仓库的 species.json 和 field-guide.zh-Hans.json，加上它们所在的提交
python3 site/build_site.py docs/picks.csv docs/eye-check.csv <species.json> <field-guide.zh-Hans.json> <花叔提交> docs work/photos
# 对标检查
python3 <ivan-parity>/scripts/parity_check.py parity.json --out PARITY.md
```

采集脚本按 iNaturalist 的建议限速：每次请求间隔约 1 秒，每 24 小时不超过 8,000 次。

## 授权

- 代码（`scripts/`）：MIT，见 [LICENSE](LICENSE)。
- 本项目整理的数据（`docs/*.csv`、`docs/stats.json`）：CC BY 4.0。
- 照片：版权归各自摄影师，授权逐张列在 `docs/picks.csv`，本仓库只链接、不存放照片。
- 花叔的贴纸：CC BY 4.0，作者花叔，来自 [huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)，固定在提交 fc3d958（数据 2.2.0），页面只链接、不存放。

详见 [NOTICE.md](NOTICE.md)。
