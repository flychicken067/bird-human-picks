import SwiftUI
#if canImport(UIKit)
import UIKit
typealias PlatformImage = UIImage
extension Image { init(platformImage: UIImage) { self.init(uiImage: platformImage) } }
#else
import AppKit
typealias PlatformImage = NSImage
extension Image { init(platformImage: NSImage) { self.init(nsImage: platformImage) } }
#endif

/// One species and the photo chosen for it. Everything here ships inside the app; nothing is fetched.
struct Bird: Codable, Identifiable, Hashable {
    let id: String
    let zh: String
    let en: String
    let sci: String
    var order: String? = nil
    var family: String? = nil
    let agree: Int
    let months: Int
    var observation: String? = nil
    var licence: String? = nil
    var credit: String? = nil

    var name: String { zh.isEmpty ? en : zh }
    var evidence: String { "\(agree) 人认定 · 跨 \(months) 个月" }
}

enum BirdData {
    /// Reads birds.json from the given bundle (the app and the widget each ship their own copy).
    static func load(_ bundle: Bundle = .main) -> [Bird] {
        guard let url = bundle.url(forResource: "birds", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let birds = try? JSONDecoder().decode([Bird].self, from: data) else { return [] }
        return birds
    }

    static func image(_ bird: Bird, folder: String, bundle: Bundle = .main) -> PlatformImage? {
        guard let url = bundle.url(forResource: bird.id, withExtension: "jpg", subdirectory: folder) else { return nil }
        return PlatformImage(contentsOfFile: url.path)
    }

    /// Same bird for everyone on the same day, in the app and in the widget.
    static func today(_ birds: [Bird], date: Date = .now) -> Bird? {
        guard !birds.isEmpty else { return nil }
        var cal = Calendar(identifier: .gregorian)
        cal.timeZone = .current
        let start = cal.date(from: DateComponents(year: 2026, month: 1, day: 1))!
        let days = cal.dateComponents([.day], from: start, to: cal.startOfDay(for: date)).day ?? 0
        let n = birds.count
        return birds[((days * 7919) % n + n) % n]  // step by a prime so neighbours in the list are not neighbours in time
    }
}
