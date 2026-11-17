from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Allowed crew ranks."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Validated model representing one mission crew member."""

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Validated model representing a mission and its crew."""

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Validate mission-wide safety and operational requirements."""
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_leader = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        experienced_crew = sum(
            member.years_experience >= 5 for member in self.crew
        )
        if self.duration_days > 365 and experienced_crew * 2 < len(self.crew):
            raise ValueError(
                "Long missions need at least 50% experienced crew"
            )

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def print_validation_error(error: ValidationError) -> None:
    """Print only the clearest validation message."""
    first_error = error.errors()[0]
    message = str(first_error["msg"])
    message = message.removeprefix("Value error, ")
    print(message)


def display_mission(mission: SpaceMission) -> None:
    """Print a space mission and its crew in a clear format."""
    print("Mission:", mission.mission_name)
    print("ID:", mission.mission_id)
    print("Destination:", mission.destination)
    print("Duration:", mission.duration_days, "days")
    print("Budget:", f"${mission.budget_millions}M")
    print("Crew size:", len(mission.crew))
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )


def main() -> None:
    """Demonstrate valid and invalid space mission validation."""
    print("Space Mission Crew Validation")
    print("=" * 42)

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2026, 7, 1, 9, 0, 0),
        duration_days=900,
        crew=[
            CrewMember(
                member_id="SC001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=42,
                specialization="Mission Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="JS002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=35,
                specialization="Navigation",
                years_experience=7,
            ),
            CrewMember(
                member_id="AJ003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=31,
                specialization="Engineering",
                years_experience=6,
            ),
        ],
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    display_mission(valid_mission)

    print("=" * 41)
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Training Flight",
            destination="Moon Base",
            launch_date=datetime(2026, 7, 2, 9, 0, 0),
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="TR001",
                    name="Taylor Reed",
                    rank=Rank.LIEUTENANT,
                    age=28,
                    specialization="Navigation",
                    years_experience=3,
                )
            ],
            budget_millions=100.0,
        )
    except ValidationError as error:
        print_validation_error(error)


if __name__ == "__main__":
    main()
