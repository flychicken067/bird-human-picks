import SwiftUI

struct BirdDetail: View {
    @EnvironmentObject private var store: Store
    let bird: Bird

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
                    Text([bird.order, bird.family].compactMap { $0 }.joined(separator: " · "))
                        .font(.footnote).foregroundStyle(.secondary)
                }
                GroupBox {
                    VStack(alignment: .leading, spacing: 6) {
                        Label(bird.evidence, systemImage: "person.3")
                            .font(.headline)
                        Text("这张照片在 iNaturalist 上由 \(bird.agree) 个账号认定为这个物种，认定跨 \(bird.months) 个不同月份，没有人给出其他物种。")
                            .font(.callout)
                            .foregroundStyle(.secondary)
                    }
                    .frame(maxWidth: .infinity, alignment: .leading)
                }
                VStack(alignment: .leading, spacing: 4) {
                    Text("照片：\(bird.credit ?? "")").font(.footnote)
                    Text("授权：\(bird.licence ?? "")").font(.footnote).foregroundStyle(.secondary)
                    if let s = bird.observation, let url = URL(string: s) {
                        Link("在 iNaturalist 查看这条观测（需联网）", destination: url).font(.footnote)
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
