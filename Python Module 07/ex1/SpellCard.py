from ex0.Card import Card
from typing import Dict, Any


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.effect_type}"
        }

    def resolve_effect(self, targets: list) -> Dict[str, Any]:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": [target.name for target in targets],
            "effect_resolved": True
        }

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info["effect_type"] = self.effect_type
        info["type"] = "Spell"
        return info
