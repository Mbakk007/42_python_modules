from ex0.Card import Card
from typing import Dict, Any
from enum import Enum


class EffectType(Enum):
    DAMAGE = "Deal 3 damage to target"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)

        try:
            self.effect_type = EffectType(effect_type)
        except ValueError:
            raise ValueError("Invalid effect type")

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.effect_type.value}"
        }

    def resolve_effect(self, targets: list) -> Dict[str, Any]:
        return {
            "spell": self.name,
            "effect_type": self.effect_type.value,
            "targets": [target.name for target in targets],
            "effect_resolved": True
        }

    def get_card_info(self) -> Dict[str, Any]:
        info = super().get_card_info()
        info["effect_type"] = self.effect_type.value
        info["type"] = "Spell"
        return info
