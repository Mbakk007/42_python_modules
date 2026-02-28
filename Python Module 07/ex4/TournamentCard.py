from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        power: int,
        base_rating: int = 1200
    ) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.power = power

        self.wins = 0
        self.losses = 0
        self.rating = base_rating

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card played"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.card_id,
            "target": target.card_id,
            "damage_dealt": self.power,
            "combat_resolved": True
        }

    def defend(self, attacker) -> dict:
        return {
            "defender": self.card_id,
            "attacker": attacker.card_id,
            "defended": True
        }

    def get_combat_stats(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "power": self.power
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": str(self.wins) + "-" + str(self.losses)
        }

    def _apply_match_result(self, won: bool) -> None:
        change = 26
        if won:
            self.update_wins(1)
            self.rating += change
        else:
            self.update_losses(1)
            self.rating -= change
