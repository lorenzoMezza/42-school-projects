"""Factory classes for exercise 0."""

from abc import ABC, abstractmethod

from ex0.creatures import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    """Abstract factory able to create a Creature family."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base Creature of a family."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved Creature of a family."""


class FlameFactory(CreatureFactory):
    """Factory for the fire family."""

    def create_base(self) -> Creature:
        """Create a base fire Creature."""
        return Flameling()

    def create_evolved(self) -> Creature:
        """Create an evolved fire Creature."""
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for the water family."""

    def create_base(self) -> Creature:
        """Create a base water Creature."""
        return Aquabub()

    def create_evolved(self) -> Creature:
        """Create an evolved water Creature."""
        return Torragon()
