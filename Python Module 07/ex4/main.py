from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Rare", 10, 1200)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Uncommon", 8, 1150)

    platform.register_card(dragon)
    platform.register_card(wizard)

    print("Fire Dragon (ID: dragon_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", dragon.rating)
    print("- Record:", str(dragon.wins) + "-" + str(dragon.losses))

    print("Ice Wizard (ID: wizard_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", wizard.rating)
    print("- Record:", str(wizard.wins) + "-" + str(wizard.losses))

    print("Creating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result)

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()

    place = 1
    for card in leaderboard:
        print(str(place) + ". " + card.name + " - Rating: " +
              str(card.rating) + " (" + str(card.wins) +
              "-" + str(card.losses) + ")")
        place += 1

    print("Platform Report:")
    print(platform.generate_tournament_report())

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
