from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Factory: FantasyCardFactory")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print("Available types:", factory.get_supported_types())

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")

    names = []
    for card in engine.hand:
        names.append(card.name)
    print("Hand:", names)

    turn_result = engine.simulate_turn()

    print("\nTurn execution:")
    print("Strategy:", turn_result["Strategy"])
    print("Actions:", turn_result["Actions"])

    print("\nGame Report:")
    print(engine.get_engine_status())


if __name__ == "__main__":
    main()
