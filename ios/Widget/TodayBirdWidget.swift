import SwiftUI
import WidgetKit

struct TodayEntry: TimelineEntry {
    let date: Date
    let bird: Bird?
}

struct TodayProvider: TimelineProvider {
    private let birds = BirdData.load()

    func placeholder(in context: Context) -> TodayEntry { TodayEntry(date: .now, bird: birds.first) }

    func getSnapshot(in context: Context, completion: @escaping (TodayEntry) -> Void) {
        completion(TodayEntry(date: .now, bird: BirdData.today(birds)))
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<TodayEntry>) -> Void) {
        let cal = Calendar.current
        let today = cal.startOfDay(for: .now)
        let entries = (0..<7).map { offset -> TodayEntry in
            let day = cal.date(byAdding: .day, value: offset, to: today)!
            return TodayEntry(date: day, bird: BirdData.today(birds, date: day))
        }
        completion(Timeline(entries: entries, policy: .atEnd))
    }
}

struct TodayBirdView: View {
    let entry: TodayEntry
    var body: some View {
        if let bird = entry.bird {
            ZStack(alignment: .bottomLeading) {
                LinearGradient(colors: [.clear, .black.opacity(0.7)], startPoint: .center, endPoint: .bottom)
                VStack(alignment: .leading, spacing: 1) {
                    Text("今日一鸟").font(.caption2.weight(.semibold))
                    Text(bird.name).font(.headline).lineLimit(1)
                    Text(bird.evidence).font(.caption2).lineLimit(1)
                }
                .foregroundStyle(.white)
            }
            .containerBackground(for: .widget) {
                if let img = BirdData.image(bird, folder: "Thumbs") {
                    Image(platformImage: img).resizable().scaledToFill()
                } else {
                    Color.gray
                }
            }
        } else {
            Text("没有数据").containerBackground(.fill, for: .widget)
        }
    }
}

@main
struct TodayBirdWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(kind: "TodayBird", provider: TodayProvider()) { TodayBirdView(entry: $0) }
            .configurationDisplayName("今日一鸟")
            .description("每天一种鸟，照片由多人认定。")
            .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}
