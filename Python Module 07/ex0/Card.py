from abc import ABC, abstractmethod
from typing import Dict, Any
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    UNCOMMON = "Uncommon"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        try:
            self.rarity = Rarity(rarity)
        except ValueError:
            raise ValueError("Invalid rarity type")

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def get_card_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value
        }

    def is_playable(self, available_mana: int) -> bool:
        if self.cost > available_mana:
            return False
        return True
