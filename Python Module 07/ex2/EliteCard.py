from typing import Any, Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 defense: int, mana: int, combat_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.defense_power = defense
        self.mana = mana
        self.combat_type = combat_type

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return game_state

    def attack(self, target: str | Any) -> Dict[str, Any]:
        return {"attacker": self.name, "target": target,
                "damage": self.attack_power, "combat_type": self.combat_type}

    def cast_spell(self, spell_name: str, targets: list) -> Dict[str, Any]:
        self.mana -= self.cost
        return {"caster": self.name, "spell": spell_name,
                "targets": targets, "mana_used": self.cost}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_blocked = min(self.defense_power, incoming_damage)
        damage_taken = max(0, incoming_damage - self.defense_power)
        return {"defender": self.name,
                "damage_taken": damage_taken,
                "damage_blocked": damage_blocked,
                "still_alive": True
                if damage_taken < self.defense_power else False}

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_combat_stats(self) -> Dict[str, Any]:
        stats = {"attack": self.attack_power, "defense": self.defense_power}
        return stats

    def get_magic_stats(self) -> Dict[str, Any]:
        stats = {"mana": self.mana, "spell_power": 7}
        return stats
