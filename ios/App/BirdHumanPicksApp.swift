import SwiftUI

@main
struct BirdHumanPicksApp: App {
    @StateObject private var store = Store()
    var body: some Scene {
        WindowGroup {
            ContentView().environmentObject(store)
        }
    }
}

@MainActor
final class Store: ObservableObject {
    let birds: [Bird] = BirdData.load()
    @Published var favorites: Set<String> {
        didSet { UserDefaults.standard.set(Array(favorites), forKey: "favorites") }
    }
    init() { favorites = Set(UserDefaults.standard.stringArray(forKey: "favorites") ?? []) }

    func toggle(_ bird: Bird) {
        if favorites.contains(bird.id) { favorites.remove(bird.id) } else { favorites.insert(bird.id) }
    }
}
