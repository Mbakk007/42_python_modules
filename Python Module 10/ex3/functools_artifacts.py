from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable, List, Dict, Any


def spell_reducer(spells: List[int], operation: str) -> int:
    """functools.reduce takes a list of ints and an operation,
            and applies the operation to each element in the list."""
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError("Choose from 'add', 'multiply', 'max', 'min'.")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    """functools.partial takes a function and some arguments, and returns a
        new function that calls the original function with those arguments."""
    if not callable(base_enchantment):
        raise ValueError("Base enchantment must be a callable function.")

    return {
        "fire_enchant":      partial(base_enchantment,
                                     power=50,
                                     element="fire"),
        "ice_enchant":       partial(base_enchantment,
                                     power=50,
                                     element="ice"),
        "lightning_enchant": partial(base_enchantment,
                                     power=50,
                                     element="lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """functools.lru_cache is a decorator that caches the results of a function
        so that it doesn't have to recompute the same result when recalled."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """functools.singledispatch is a decorator that allows you to create
            a function that returns different results based on
                the type of the first argument."""
    @singledispatch
    def dispatch_spell(spell) -> str | List[Any] | int:
        return "Unsupported type."

    @dispatch_spell.register(int)
    def int_spell(spell: int):
        return f"Damage spell with power {spell}."

    @dispatch_spell.register(str)
    def str_spell(spell: str):
        return f"Enchantment spell: {spell}."

    @dispatch_spell.register(list)
    def list_spell(spell: list[int | str]):
        return [dispatch_spell(s) for s in spell]

    return dispatch_spell


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # time to compute fib is reduced each time due to caching

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(25))
    print(dispatcher("Invisibility"))
    print(dispatcher([10, "Strength", 20, "Agility"]))

    print("\nTesting partial enchanter...")
    base_enchantment = (lambda power, element, target:
                        f"{element} enchanted on {target} with power {power}")
    enchanter = partial_enchanter(base_enchantment)
    print(enchanter["fire_enchant"](target="Sword"))
    print(enchanter["ice_enchant"](target="Shield"))
    print(enchanter["lightning_enchant"](target="Armor"))
