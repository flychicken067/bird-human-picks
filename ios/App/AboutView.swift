import SwiftUI

struct AboutView: View {
    @Environment(\.dismiss) private var dismiss
    @EnvironmentObject private var store: Store

    var body: some View {
        NavigationStack {
            List {
                Section("这是什么") {
                    Text("每种鸟一张真实的野外照片。照片来自 iNaturalist，每张都有至少 3 个人在至少 3 个不同月份认定为同一物种，而且没有人给出其他物种。共收录 \(store.birds.count) 种。")
                }
                Section("怎么选的") {
                    Text("照片授权必须是 CC0、CC BY 或 CC BY-SA，原图足够清晰。先由检测模型筛掉画面里有多只鸟、鸟太小或有人手的照片，再逐张人工看图，排除被遮挡、死鸟、家禽、手绘画等。模型只看画面，不判断物种；物种以人的鉴定为准。")
                }
                Section("局限") {
                    Text("3 个账号不等于 3 位专家，他们也可能跟随别人的鉴定。如果发现哪张图不对，欢迎到 GitHub 提 issue。")
                }
                Section("隐私") {
                    Text("全部内容都在 App 里，离线可用。App 不联网、不收集任何数据，收藏只保存在本机。")
                }
                Section("开源与授权") {
                    Link("项目主页：github.com/flychicken067/bird-human-picks", destination: URL(string: "https://github.com/flychicken067/bird-human-picks")!)
                    Text("照片版权归各自摄影师，作者和授权写在每种鸟的页面上。物种名称和分类来自 huashu-bird-sticker 的数据（MIT）。")
                }
            }
            .navigationTitle("关于")
            .toolbar { ToolbarItem { Button("完成") { dismiss() } } }
        }
    }
}
