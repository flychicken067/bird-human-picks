import SwiftUI

private struct Section<Content: View>: View {
    let title: String
    @ViewBuilder var content: Content
    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(title).font(.headline)
            content
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}

struct BirdDetail: View {
    @EnvironmentObject private var store: Store
    let bird: Bird

    private var taxonLine: String {
        let family = [bird.zhFamily, bird.family].compactMap { $0 }.joined(separator: " ")
        let order = [bird.zhOrder, bird.order].compactMap { $0 }.joined(separator: " ")
        return [family, order].filter { !$0.isEmpty }.joined(separator: " · ")
    }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                if let img = BirdData.image(bird, folder: "Photos") {
                    Image(platformImage: img)
                        .resizable()
                        .scaledToFit()
                        .frame(maxWidth: .infinity)
                        .clipShape(RoundedRectangle(cornerRadius: 12))
                        .accessibilityLabel("\(bird.name)的照片")
                }
                VStack(alignment: .leading, spacing: 4) {
                    Text(bird.name).font(.largeTitle.weight(.bold))
                    Text(bird.sci).font(.title3).italic().foregroundStyle(.secondary)
                    if !bird.zh.isEmpty { Text(bird.en).foregroundStyle(.secondary) }
                    Text(taxonLine).font(.footnote).foregroundStyle(.secondary)
                }
                GroupBox {
                    VStack(alignment: .leading, spacing: 6) {
                        Label(bird.evidence, systemImage: "person.3")
                            .font(.headline)
                        Text("这张照片在 iNaturalist 上由 \(bird.agree) 个账号认定为这个物种，认定跨 \(bird.months) 个不同月份，没有人给出其他物种。")
                            .font(.callout)
                            .foregroundStyle(.secondary)
                        Text("真实照片，不是 AI 生成。物种由 iNaturalist 用户鉴定，人也会出错。")
                            .font(.footnote)
                            .foregroundStyle(.secondary)
                    }
                    .frame(maxWidth: .infinity, alignment: .leading)
                }
                if bird.impression != nil || bird.marks != nil {
                    Section(title: "图鉴笔记") {
                        if let s = bird.impression { Text(s) }
                        ForEach(bird.marks ?? [], id: \.self) { Text("· " + $0).foregroundStyle(.secondary) }
                        Text("文字来自 huashu-bird-sticker 的中文图鉴笔记，CC BY-SA 4.0。").font(.caption).foregroundStyle(.tertiary)
                    }
                }
                let size = [("体长", bird.length), ("翼展", bird.wingspan), ("体重", bird.weight)].compactMap { k, v in v.map { (k, $0) } }
                if !size.isEmpty {
                    Section(title: "体型") {
                        ForEach(size, id: \.0) { k, v in
                            HStack { Text(k).foregroundStyle(.secondary).frame(width: 44, alignment: .leading); Text(v) }
                        }
                    }
                }
                if let code = bird.iucn, let name = bird.iucnName {
                    Section(title: "IUCN 保护等级") { Text("\(code) · \(name)") }
                }
                if let r = bird.range {
                    Section(title: "分布") { Text(r) }
                }
                VStack(alignment: .leading, spacing: 6) {
                    Text("照片：\(bird.credit ?? "")").font(.footnote)
                    Text("授权：\(bird.licence ?? "")").font(.footnote).foregroundStyle(.secondary)
                    if let s = bird.observation, let url = URL(string: s) {
                        Link("在 iNaturalist 查看这条观测（需联网）", destination: url).font(.footnote)
                    }
                    if let url = bird.reportURL {
                        Link("这张图不对？到 GitHub 报错（需联网）", destination: url).font(.footnote)
                    }
                }
            }
            .padding()
        }
        .navigationTitle(bird.name)
        #if os(iOS)
        .navigationBarTitleDisplayMode(.inline)
        #endif
        .toolbar {
            ToolbarItem {
                Button { store.toggle(bird) } label: {
                    Image(systemName: store.favorites.contains(bird.id) ? "star.fill" : "star")
                }
                .accessibilityLabel(store.favorites.contains(bird.id) ? "取消收藏" : "收藏")
            }
        }
    }
}
