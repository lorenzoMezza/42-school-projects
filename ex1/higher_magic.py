"""Exercise 1 - Higher Realm."""

from collections.abc import Callable
from typing import Any

Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Build a spell that executes two spells with identical arguments."""
    def combined(target: str, power: int) -> tuple[Any, Any]:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Build a spell that multiplies its received power before casting."""
    def amplified(target: str, power: int) -> Any:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Build a spell that only runs when condition accepts its arguments."""
    def conditional_spell(target: str, power: int) -> Any:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    """Build a spell that casts every supplied spell in order."""
    def sequence(target: str, power: int) -> list[Any]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", ", ".join(combined("Dragon", 10)))
    print("Testing power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print("Original:", fireball("Dragon", 10))
    print("Amplified:", amplified("Dragon", 10))
    print("Conditional:", conditional_caster(lambda _t, p: p >= 10, heal)("Mage", 5))
    print("Sequence:", spell_sequence([fireball, heal])("Ogre", 12))
