from functools import wraps
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    """@wraps preserves the original function's metadata."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) < 3:
                return "No power level provided"
            power = args[2]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    print(f"Spell failed, retrying... (attempt"
                          f"{attempts}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for char in name:
            if not (char.isalpha() or char.isspace()):
                return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"
# static methods can access the class without creating an instance
# instance methods require an instance of the class (self parameter)


if __name__ == "__main__":
    print("\nTesting spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"
    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Dragon"))
    print(MageGuild.validate_mage_name("dr"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Heal", 5))

    print("\nTesting retry spell...")

    @retry_spell(max_attempts=10)
    def unstable_spell():
        if time.time() % 2 < 1:
            time.sleep(0.2)
            raise ValueError("Spell fizzled!")
        return "Spell succeeded!"
    print(unstable_spell())
