from typing import Callable, Any
""" nonlocal allows the inner function to modify the variable
        defined in the outer function's scope."""


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    memory_storage = {}

    def store(key: str, value) -> None:
        memory_storage[key] = value

    def recall(key: str) -> Any:
        if key in memory_storage:
            return memory_storage[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(10)
    print(f"After adding 5: {accumulator(5)}")
    print(f"After adding 10: {accumulator(10)}")

    print("\nTesting enchantment factory...")
    flaming_enchant = enchantment_factory("Flaming")
    frozen_enchant = enchantment_factory("Frozen")
    print(flaming_enchant("Sword"))
    print(frozen_enchant("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"](key="secret_spell", value="Invisibility")
    print(vault["recall"]("secret_spell"))
    print(vault["recall"]("not_found"))
