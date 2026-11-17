"""Battle strategies for exercise 2."""

from abc import ABC, abstractmethod
from typing import List

from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is applied to an invalid Creature."""


class BattleStrategy(ABC):
    """Abstract battle strategy."""

    strategy_name: str

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return whether this strategy can be used by the Creature."""

    @abstractmethod
    def act(self, creature: Creature) -> List[str]:
        """Return all action messages for this Creature's turn."""


class NormalStrategy(BattleStrategy):
    """Strategy that only attacks."""

    strategy_name = "normal"

    def is_valid(self, creature: Creature) -> bool:
        """Normal strategy accepts every Creature."""
        return True

    def act(self, creature: Creature) -> List[str]:
        """Attack once."""
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    """Strategy for transforming Creatures."""

    strategy_name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        """Return whether the Creature can transform."""
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> List[str]:
        """Transform, attack and revert."""
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                "Invalid Creature "
                f"'{creature.name}' for this aggressive strategy"
            )
        return [
            creature.transform(),
            creature.attack(),
            creature.revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    """Strategy for healing Creatures."""

    strategy_name = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        """Return whether the Creature can heal."""
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> List[str]:
        """Attack and heal."""
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                "Invalid Creature "
                f"'{creature.name}' for this defensive strategy"
            )
        return [creature.attack(), creature.heal()]
