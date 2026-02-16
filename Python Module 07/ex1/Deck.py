from ex0.Card import Card
from typing import Dict, Any
import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Deck is empty")

        card = self.cards[0]
        self.cards.remove(card)
        return card

    def get_deck_stats(self) -> Dict[str, Any]:
        stats = {
            "total_cards": len(self.cards),
            "card_names": [card.name for card in self.cards]
        }
        return stats
