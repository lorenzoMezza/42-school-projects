"""Public interface for exercise 2."""

from ex2.strategies import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

__all__ = [
    "AggressiveStrategy",
    "BattleStrategy",
    "DefensiveStrategy",
    "InvalidStrategyError",
    "NormalStrategy",
]
