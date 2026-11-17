"""Capability abstract classes for exercise 1."""

from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract healing capability."""

    @abstractmethod
    def heal(self) -> str:
        """Return a healing action message."""


class TransformCapability(ABC):
    """Abstract transformation capability with persistent state."""

    def __init__(self) -> None:
        """Initialize the transformation state."""
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        """Transform the object and return an action message."""

    @abstractmethod
    def revert(self) -> str:
        """Revert the transformation and return an action message."""
