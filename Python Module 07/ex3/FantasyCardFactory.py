from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            return CreatureCard(name_or_power, 3, "Common", 2, 3)

        return CreatureCard("Goblin Warrior", 4, "Common", 2, 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            return SpellCard(name_or_power, 3, "Common", "Magic")

        return SpellCard("Lightning Bolt", 3, "Common", "Lightning")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            return ArtifactCard(name_or_power, 1, "Common", 3, "Mana boost")

        return ArtifactCard("Mana Ring", 1, "Common", 3, "Mana boost")

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        i = 0
        while i < size:
            if i % 3 == 0:
                cards.append(self.create_creature())
            elif i % 3 == 1:
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
            i += 1
        return {"theme": "Fantasy", "cards": cards}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "lightning_bolt"],
            "artifacts": ["mana_ring"],
        }
