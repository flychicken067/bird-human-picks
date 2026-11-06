# 人选鸟图 iOS App

离线图鉴：每种鸟一张由多人认定的野外照片，数据和 `docs/picks.csv` 相同。App 不联网、不收集数据，收藏只存在本机。附带「今日一鸟」桌面小组件。

## 构建

需要 Xcode 16 以上和 [XcodeGen](https://github.com/yonaskolb/XcodeGen)。

```sh
cd ios
python3 scripts/make_bundle.py ../docs/picks.csv photo-cache Resources   # 下载照片并缩放，约 55 MB
xcodegen generate
open BirdHumanPicks.xcodeproj
```

在 `project.yml` 里填上自己的 `DEVELOPMENT_TEAM`，或在 Xcode 的 Signing 里选择团队。

App 图标用的是冠翠鸟照片（iNaturalist 观测 [9765521 号照片](https://www.inaturalist.org/photos/9765521)，CC0）。
