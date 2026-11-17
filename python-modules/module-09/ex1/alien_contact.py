from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Allowed alien contact types."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Validated model representing an alien contact report."""

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        """Validate business rules that depend on multiple fields."""
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals should include received messages"
            )

        return self


def print_validation_error(error: ValidationError) -> None:
    """Print only the clearest validation message."""
    first_error = error.errors()[0]
    message = str(first_error["msg"])
    message = message.removeprefix("Value error, ")
    print(message)


def display_contact(contact: AlienContact) -> None:
    """Print an alien contact report clearly."""
    print("ID:", contact.contact_id)
    print("Type:", contact.contact_type.value)
    print("Location:", contact.location)
    print("Signal:", f"{contact.signal_strength}/10")
    print("Duration:", contact.duration_minutes, "minutes")
    print("Witnesses:", contact.witness_count)

    if contact.message_received is not None:
        print("Message:", repr(contact.message_received))

    print("Verified:", contact.is_verified)


def main() -> None:
    """Demonstrate valid and invalid alien contact validation."""
    print("Alien Contact Log Validation")
    print("=" * 38)

    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2026, 6, 19, 14, 30, 0),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )

    print("Valid contact report:")
    display_contact(valid_contact)

    print("=" * 38)
    print("Expected validation error:")

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2026, 6, 19, 15, 0, 0),
            location="Lunar Outpost",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=4.2,
            duration_minutes=15,
            witness_count=1,
        )
    except ValidationError as error:
        print_validation_error(error)


if __name__ == "__main__":
    main()
