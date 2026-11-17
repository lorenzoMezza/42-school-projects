"""Creature classes with capabilities for exercise 1."""

from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Base healing Creature."""

    def __init__(self) -> None:
        """Initialize Sproutling."""
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        """Return Sproutling's attack."""
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        """Return Sproutling's healing action."""
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Evolved healing Creature."""

    def __init__(self) -> None:
        """Initialize Bloomelle."""
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        """Return Bloomelle's attack."""
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        """Return Bloomelle's healing action."""
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Base transforming Creature."""

    def __init__(self) -> None:
        """Initialize Shiftling."""
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Return Shiftling's attack depending on its state."""
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        """Transform Shiftling."""
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        """Revert Shiftling."""
        self.transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    """Evolved transforming Creature."""

    def __init__(self) -> None:
        """Initialize Morphagon."""
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Return Morphagon's attack depending on its state."""
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        """Transform Morphagon."""
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        """Revert Morphagon."""
        self.transformed = False
        return "Morphagon stabilizes its form."
