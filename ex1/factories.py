"""Factories for exercise 1 Creature families."""

from ex0.creatures import Creature
from ex0.factories import CreatureFactory
from ex1.creatures import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    """Factory for healing Creatures."""

    def create_base(self) -> Creature:
        """Create the base healing Creature."""
        return Sproutling()

    def create_evolved(self) -> Creature:
        """Create the evolved healing Creature."""
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Factory for transforming Creatures."""

    def create_base(self) -> Creature:
        """Create the base transforming Creature."""
        return Shiftling()

    def create_evolved(self) -> Creature:
        """Create the evolved transforming Creature."""
        return Morphagon()
