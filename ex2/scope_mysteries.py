"""Exercise 2 - Memory Depths."""

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def count_call() -> int:
        nonlocal count
        count += 1
        return count

    return count_call


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def add_power(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memories: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memories[key] = value

    def recall(key: str) -> Any:
        return memories.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())
    print("Testing spell accumulator...")
    accumulate = spell_accumulator(100)
    print("Base 100, add 20:", accumulate(20))
    print("Base 100, add 30:", accumulate(30))
    print("Testing enchantment factory...")
    print(enchantment_factory("Flaming")("Sword"))
    print(enchantment_factory("Frozen")("Shield"))
    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))
