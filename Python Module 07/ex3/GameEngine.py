from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []

        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        deck = self.factory.create_themed_deck(3)
        self.hand = deck["cards"]
        self.battlefield = []

        self.cards_created = len(self.hand)
        self.turns_simulated = 0
        self.total_damage = 0

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            raise Exception("Engine not configured with factory and strategy")

        self.turns_simulated += 1
        turn_result = self.strategy.execute_turn(self.hand, self.battlefield)

        return turn_result

    def get_engine_status(self) -> dict:
        strategy_name = ""
        if self.strategy is not None:
            strategy_name = self.strategy.get_strategy_name()

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
