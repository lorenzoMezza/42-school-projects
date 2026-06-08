import random


ACHIEVEMENTS = [
    "First Steps",
    "Master Explorer",
    "Boss Slayer",
    "Treasure Hunter",
    "Speed Runner",
    "Crafting Genius",
    "World Savior",
    "Hidden Path Finder",
    "Collector Supreme",
    "Unstoppable",
    "Untouchable",
    "Strategist",
    "Survivor",
    "Sharp Mind",
]

PLAYERS = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set[str]:
    amount = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, amount))


def get_all_distinct(player_sets: dict[str, set[str]]) -> set[str]:
    all_distinct: set[str] = set()
    for achievements in player_sets.values():
        all_distinct = all_distinct.union(achievements)
    return all_distinct


def get_common(player_sets: dict[str, set[str]]) -> set[str]:
    common = set(ACHIEVEMENTS)
    for achievements in player_sets.values():
        common = common.intersection(achievements)
    return common


def get_others(player_sets: dict[str, set[str]], player: str) -> set[str]:
    others: set[str] = set()
    for other_player in player_sets:
        if other_player != player:
            others = others.union(player_sets[other_player])
    return others


def main() -> None:
    print("=== Achievement Tracker System ===")
    player_sets: dict[str, set[str]] = {}
    for player in PLAYERS:
        player_sets[player] = gen_player_achievements()
        print(f"Player {player}: {player_sets[player]}")

    all_achievements = set(ACHIEVEMENTS)
    print(f"All distinct achievements: {get_all_distinct(player_sets)}")
    print(f"Common achievements: {get_common(player_sets)}")

    for player in PLAYERS:
        others = get_others(player_sets, player)
        only_player_has = player_sets[player].difference(others)
        print(f"Only {player} has: {only_player_has}")

    for player in PLAYERS:
        missing = all_achievements.difference(player_sets[player])
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
