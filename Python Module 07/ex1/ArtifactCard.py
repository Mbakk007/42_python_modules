from ex0.Card import Card
from typing import Dict, Any


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("Durability must be a positive integer.")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> Dict[str, Any]:
        if self.durability > 0:
            self.durability -= 1
            return {
                "card": self.name,
                "ability_activated": True,
                "remaining_durability": self.durability,
                "effect": f"{self.effect}"
            }
        else:
            return {
                "card": self.name,
                "ability_activated": False,
                "reason": "Artifact is broken and cannot be activated."
            }
