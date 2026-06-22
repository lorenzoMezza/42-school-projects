"""Exercise 0 - Lambda Sanctum."""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Return artifacts ordered by descending power."""
    return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Return only mages whose power reaches min_power."""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap every spell name in the requested magic markers."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Compute maximum, minimum and average mage power."""
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    max_mage = max(mages, key=lambda mage: mage["power"])
    min_mage = min(mages, key=lambda mage: mage["power"])
    average = round(sum(map(lambda mage: mage["power"], mages)) / len(mages), 2)
    return {
        "max_power": max_mage["power"],
        "min_power": min_mage["power"],
        "avg_power": average,
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
    ]
    print("Testing artifact sorter...")
    ordered = artifact_sorter(artifacts)
    print(f"{ordered[0]['name']} ({ordered[0]['power']} power) comes before "
          f"{ordered[1]['name']} ({ordered[1]['power']} power)")
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(["fireball", "heal", "shield"])))
