from typing import Callable, Tuple
"""Callable() is used to verify that a parameter is a
                function that can be called."""
""" *args and **kwargs allow the function to accept
                any number of arguments and keyword arguments."""


"""Implementation Requirements
spell_combiner(spell1, spell2) - Combine two spells:
• Return a new function that calls both spells with the same arguments
• The combined spell should return a tuple of both results
• Example: combined = spell_combiner(fireball, heal)
power_amplifier(base_spell, multiplier) - Amplify spell power:
• Return a new function that multiplies the base spell's result by multiplier
• Assume base spell returns a number (damage, healing, etc.)
• Example: mega_fireball = power_amplifier(fireball, 3)
conditional_caster(condition, spell) - Cast spell conditionally:
• Return a function that only casts the spell if condition returns True
• If condition fails, return "Spell fizzled"
• Both condition and spell receive the same arguments
spell_sequence(spells) - Create spell sequence:
• Return a function that casts all spells in order
• Each spell receives the same arguments
• Return a list of all spell results"""


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
