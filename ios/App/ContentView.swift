import SwiftUI

struct ContentView: View {
    @EnvironmentObject private var store: Store
    @State private var query = ""
    @State private var onlyFavorites = false
    @State private var showAbout = false

    private var shown: [Bird] {
        let q = query.trimmingCharacters(in: .whitespaces).lowercased()
        return store.birds.filter { b in
            (!onlyFavorites || store.favorites.contains(b.id)) &&
            (q.isEmpty || [b.zh, b.en, b.sci, b.family ?? ""].joined(separator: " ").lowercased().contains(q))
        }
    }

    private let columns = [GridItem(.adaptive(minimum: 150), spacing: 12)]

    var body: some View {
        NavigationStack {
            ScrollView {
                if query.isEmpty, !onlyFavorites, let bird = BirdData.today(store.birds) {
                    NavigationLink(value: bird) { TodayCard(bird: bird) }
                        .buttonStyle(.plain)
                        .padding(.horizontal)
                }
                Picker("范围", selection: $onlyFavorites) {
                    Text("全部 \(store.birds.count)").tag(false)
                    Text("收藏 \(store.favorites.count)").tag(true)
                }
                .pickerStyle(.segmented)
                .padding(.horizontal)
                if shown.isEmpty {
                    Text(onlyFavorites ? "还没有收藏。在鸟的页面点星标即可收藏。" : "没有找到这种鸟。")
                        .foregroundStyle(.secondary)
                        .padding(.top, 40)
                }
                LazyVGrid(columns: columns, spacing: 12) {
                    ForEach(shown) { bird in
                        NavigationLink(value: bird) { BirdCell(bird: bird) }.buttonStyle(.plain)
                    }
                }
                .padding()
            }
            .navigationTitle("人选鸟图")
            .navigationDestination(for: Bird.self) { BirdDetail(bird: $0) }
            .searchable(text: $query, prompt: "中文名、英文名、学名或科名")
            .toolbar {
                ToolbarItem {
                    Button { showAbout = true } label: { Image(systemName: "info.circle") }
                        .accessibilityLabel("关于")
                }
            }
            .sheet(isPresented: $showAbout) { AboutView() }
        }
    }
}

struct BirdPhoto: View {
    let bird: Bird
    var body: some View {
        if let img = BirdData.image(bird, folder: "Photos") {
            Image(platformImage: img).resizable().scaledToFill()
        } else {
            Color.secondary.opacity(0.15)
        }
    }
}

struct BirdCell: View {
    let bird: Bird
    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            BirdPhoto(bird: bird)
                .frame(height: 130)
                .frame(maxWidth: .infinity)
                .clipped()
                .clipShape(RoundedRectangle(cornerRadius: 10))
            Text(bird.name).font(.subheadline.weight(.semibold)).lineLimit(1)
            Text(bird.sci).font(.caption).italic().foregroundStyle(.secondary).lineLimit(1)
        }
        .accessibilityElement(children: .combine)
    }
}

struct TodayCard: View {
    let bird: Bird
    var body: some View {
        ZStack(alignment: .bottomLeading) {
            BirdPhoto(bird: bird)
                .frame(height: 220)
                .frame(maxWidth: .infinity)
                .clipped()
            LinearGradient(colors: [.clear, .black.opacity(0.65)], startPoint: .center, endPoint: .bottom)
            VStack(alignment: .leading, spacing: 2) {
                Text("今日一鸟").font(.caption.weight(.semibold))
                Text(bird.name).font(.title2.weight(.bold))
                Text(bird.evidence).font(.caption)
            }
            .foregroundStyle(.white)
            .padding()
        }
        .clipShape(RoundedRectangle(cornerRadius: 14))
        .accessibilityElement(children: .combine)
    }
}
