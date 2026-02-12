from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:")
    fire_dragon = CreatureCard(name="Fire Dragon", cost=5, rarity="Legendary",
                               attack=7, health=5)
    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    available_mana = 6
    print(f"Playable: {fire_dragon.is_playable(available_mana)}")
    play_result = fire_dragon.play(game_state={})
    print(f"Play result: {play_result}")
    print("Fire Dragon attacks Goblin Warrior:")
    goblin_warrior = CreatureCard(name="Goblin Warrior", cost=2,
                                  rarity="Common", attack=3, health=2)
    attack_result = fire_dragon.attack_target(goblin_warrior)
    print(f"Attack result: {attack_result}")
    print("Testing insufficient mana (3 available):")
    available_mana = 3
    print(f"Playable: {fire_dragon.is_playable(available_mana)}")
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
