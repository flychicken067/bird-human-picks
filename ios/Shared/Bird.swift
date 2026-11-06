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
    var zhOrder: String? = nil
    var zhFamily: String? = nil
    var length: String? = nil
    var wingspan: String? = nil
    var weight: String? = nil
    var iucn: String? = nil
    var range: String? = nil
    var impression: String? = nil
    var marks: [String]? = nil

    var name: String { zh.isEmpty ? en : zh }
    var evidence: String { "\(agree) 人认定 · 跨 \(months) 个月" }

    var iucnName: String? {
        guard let iucn else { return nil }
        return ["LC": "无危", "NT": "近危", "VU": "易危", "EN": "濒危", "CR": "极危", "EW": "野外灭绝", "EX": "灭绝", "DD": "数据缺乏"][iucn]
    }

    /// GitHub issue form with the bird and observation filled in (opens in the browser).
    var reportURL: URL? {
        var c = URLComponents(string: "https://github.com/flychicken067/bird-human-picks/issues/new")
        c?.queryItems = [URLQueryItem(name: "template", value: "wrong-photo.yml"),
                         URLQueryItem(name: "title", value: "[photo] \(sci) \(en)"),
                         URLQueryItem(name: "species", value: "\(sci) (\(zh) / \(en))"),
                         URLQueryItem(name: "photo", value: observation ?? "")]
        return c?.url
    }
}

enum BirdData {
    /// Reads birds.json from the given bundle (the app and the widget each ship their own copy).
    static func load(_ bundle: Bundle = .main) -> [Bird] {
        guard let url = bundle.url(forResource: "birds", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let birds = try? JSONDecoder().decode([Bird].self, from: data) else { return [] }
        return birds
    }

    private static let cache = NSCache<NSString, PlatformImage>()

    /// Reads a bundled photo. Cached, and cheap to call from a view body.
    static func image(_ bird: Bird, folder: String, bundle: Bundle = .main) -> PlatformImage? {
        let key = "\(folder)/\(bird.id)" as NSString
        if let hit = cache.object(forKey: key) { return hit }
        guard let base = bundle.resourceURL else { return nil }
        let path = base.appendingPathComponent(folder).appendingPathComponent(bird.id + ".jpg").path
        guard let img = PlatformImage(contentsOfFile: path) else { return nil }
        cache.setObject(img, forKey: key)
        return img
    }

    static func cached(_ bird: Bird, folder: String) -> PlatformImage? {
        cache.object(forKey: "\(folder)/\(bird.id)" as NSString)
    }

    /// Loads and decodes off the main thread, then caches.
    static func load(_ bird: Bird, folder: String) async -> PlatformImage? {
        await Task.detached(priority: .userInitiated) { () -> PlatformImage? in
            guard let img = image(bird, folder: folder) else { return nil }
            #if canImport(UIKit)
            return img.preparingForDisplay() ?? img
            #else
            return img
            #endif
        }.value
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
