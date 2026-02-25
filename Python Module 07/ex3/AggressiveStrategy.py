from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        for card in hand:
            card.play({})
            cards_played.append(card.name)
            mana_used += card.cost

            if isinstance(card, CreatureCard):
                battlefield.append(card)
                damage_dealt += card.attack

        return {
            "Strategy": self.get_strategy_name(),
            "Actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": ["Enemy Player"],
                "damage_dealt": damage_dealt
            }
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
