"""Exercise 4 - Master's Tower."""

from collections.abc import Callable
from functools import wraps
from time import perf_counter, sleep
from typing import Any


def spell_timer(func: Callable) -> Callable:
    """Decorate a spell by printing its execution duration."""
    @wraps(func)
    def timed(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        started = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - started
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return timed


def power_validator(min_power: int) -> Callable:
    """Create a decorator that rejects a spell below min_power."""
    def decorate(func: Callable) -> Callable:
        @wraps(func)
        def validated(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power is None:
                power = args[-1] if args else None
            if not isinstance(power, int) or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return validated
    return decorate


def retry_spell(max_attempts: int) -> Callable:
    """Create a decorator that retries a spell after exceptions."""
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    def decorate(func: Callable) -> Callable:
        @wraps(func)
        def retried(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return retried
    return decorate


class MageGuild:
    """A guild that validates mage names and casts validated spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """A valid mage name is at least three letters/spaces long."""
        return len(name) >= 3 and all(char.isalpha() or char == " " for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell after the decorator validates its power."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def fireball() -> str:
        sleep(0.1)
        return "Fireball cast!"

    @retry_spell(3)
    def unreliable_spell() -> str:
        raise RuntimeError("The spell failed")

    print("Testing spell timer...")
    print("Result:", fireball())
    print("Testing retrying spell...")
    print(unreliable_spell())
    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Alex"))
    print(guild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
