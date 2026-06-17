"""Creature classes for exercise 0."""

from abc import ABC, abstractmethod


class Creature(ABC):
    """Base abstract class for every Creature card."""

    def __init__(self, name: str, creature_type: str) -> None:
        """Initialize a Creature with its name and type."""
        self.name = name
        self.creature_type = creature_type

    def describe(self) -> str:
        """Return a standard description for the Creature."""
        return f"{self.name} is a {self.creature_type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        """Return the attack message of the Creature."""


class Flameling(Creature):
    """Base fire Creature."""

    def __init__(self) -> None:
        """Initialize Flameling."""
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """Return Flameling's attack."""
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """Evolved fire Creature."""

    def __init__(self) -> None:
        """Initialize Pyrodon."""
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """Return Pyrodon's attack."""
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    """Base water Creature."""

    def __init__(self) -> None:
        """Initialize Aquabub."""
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """Return Aquabub's attack."""
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    """Evolved water Creature."""

    def __init__(self) -> None:
        """Initialize Torragon."""
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """Return Torragon's attack."""
        return "Torragon uses Hydro Pump!"
