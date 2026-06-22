from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Validated model representing a monitored space station."""

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:
    """Print a space station in a clear human-readable format."""
    status = "Operational" if station.is_operational else "Not operational"

    print("ID:", station.station_id)
    print("Name:", station.name)
    print("Crew:", station.crew_size, "people")
    print("Power:", f"{station.power_level}%")
    print("Oxygen:", f"{station.oxygen_level}%")
    print("Last maintenance:", station.last_maintenance)
    print("Status:", status)
    if station.notes is not None:
        print("Notes:", station.notes)


def main() -> None:
    """Demonstrate valid and invalid space station validation."""
    print("Space Station Data Validation")
    print("=" * 40)

    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2026, 6, 19, 12, 0, 0),
        notes="All systems stable.",
    )

    print("Valid station created:")
    display_station(valid_station)

    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BAD001",
            name="Invalid Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 6, 19, 12, 0, 0),
        )
    except ValidationError as error:
        first_error = error.errors()[0]
        print(first_error["msg"])


if __name__ == "__main__":
    main()
