from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    elite = EliteCard(name="Arcane Warrior", cost=5, rarity="Legendary",
                      attack=7, defense=3, mana=4, combat_type="melee")

    print("\nPlaying Arcane Warrior (Elite Card):")
    elite.play(game_state={})
    print("\nCombat phase:")
    attack = elite.attack(target="Enemy")
    defense = elite.defend(incoming_damage=5)
    print(f"Attack result: {attack}")
    print(f"Defense result: {defense}")
    print("\nMagic phase:")
    cast = elite.cast_spell(spell_name="Fireball",
                            targets=["Enemy 1", "Enemy 2"])
    channel = elite.channel_mana(amount=3)
    print(f"Cast spell result: {cast}")
    print(f"Channel mana result: {channel}")


if __name__ == "__main__":
    main()
