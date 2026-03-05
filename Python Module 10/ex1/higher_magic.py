from typing import Callable, Tuple
"""Callable() is used to verify that a parameter is a
                function that can be called."""
""" *args and **kwargs allow the function to accept
                any number of arguments and keyword arguments."""


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise ValueError("Both parameters must be callable functions")

    def combined_spell(*args, **kwargs) -> Tuple:
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise ValueError("Base spell must be a callable function")
    if not isinstance(multiplier, int):
        raise ValueError("Multiplier must be an integer")

    def amplified_spell(*args, **kwargs) -> int | float:
        result = base_spell(*args, **kwargs)
        if not isinstance(result, (int, float)):
            raise ValueError("Base spell must return a number")
        return result * multiplier
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(spell) or not callable(condition):
        raise ValueError("Both parameters must be callable functions")

    def cast_spell(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return cast_spell


def spell_sequence(spells: list) -> Callable:
    for spell in spells:
        if not callable(spell):
            raise ValueError("All items in spells must be callable functions")

    def sequence_spell(*args, **kwargs) -> list:
        results = []
        for spell in spells:
            result = spell(*args, **kwargs)
            results.append(result)
        return results
    return sequence_spell


if __name__ == "__main__":

    print("\nTesting spell combiner...")
    combined_spell = spell_combiner(lambda target: f"Fireball hits {target}",
                                    lambda target: f"Heals {target}")
    print(combined_spell("Dragon"))

    print("\nTesting power amplifier...")
    amplified_spell = power_amplifier(lambda: 10, 3)
    print(amplified_spell())

    print("\nTesting conditional caster...")
    true_condition = conditional_caster(lambda: True, lambda: "executed")
    print(true_condition())
    false_condition = conditional_caster(lambda: False, lambda: "executed")
    print(false_condition())

    print("\nTesting spell sequence...")
    sequence = spell_sequence([
        lambda: "First spell",
        lambda: "Second spell",
        lambda: "Third spell"
    ])
    print(sequence())
