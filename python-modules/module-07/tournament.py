"""Tournament script for exercise 2."""

from typing import List, Tuple

from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex0.creatures import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = Tuple[CreatureFactory, BattleStrategy]
Fighter = Tuple[Creature, BattleStrategy]


def strategy_title(strategy: BattleStrategy) -> str:
    """Return a printable strategy name."""
    return strategy.__class__.__name__.replace("Strategy", "")


def opponent_title(opponent: Opponent) -> str:
    """Return a printable opponent tuple name."""
    factory, strategy = opponent
    if isinstance(factory, HealingCreatureFactory):
        creature_name = "Healing"
    elif isinstance(factory, TransformCreatureFactory):
        creature_name = "Transform"
    else:
        creature_name = factory.create_base().name
    return f"({creature_name}+{strategy_title(strategy)})"


def print_opponents(opponents: List[Opponent]) -> None:
    """Print the tournament opponents."""
    names = [opponent_title(opponent) for opponent in opponents]
    print("[ " + ", ".join(names) + " ]")


def build_fighters(opponents: List[Opponent]) -> List[Fighter]:
    """Create one base Creature for every opponent."""
    fighters: List[Fighter] = []
    for factory, strategy in opponents:
        fighters.append((factory.create_base(), strategy))
    return fighters


def run_actions(creature: Creature, strategy: BattleStrategy) -> None:
    """Run a strategy and print all produced actions."""
    for action in strategy.act(creature):
        print(action)


def battle(first: Fighter, second: Fighter) -> None:
    """Make two fighters battle once."""
    first_creature, first_strategy = first
    second_creature, second_strategy = second

    print("* Battle *")
    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())
    print("now fight!")
    run_actions(first_creature, first_strategy)
    run_actions(second_creature, second_strategy)


def tournament(opponents: List[Opponent]) -> None:
    """Run every opponent against every other opponent once."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    fighters = build_fighters(opponents)
    try:
        for first_index in range(len(fighters)):
            for second_index in range(first_index + 1, len(fighters)):
                battle(fighters[first_index], fighters[second_index])
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def run_named_tournament(name: str, opponents: List[Opponent]) -> None:
    """Print a tournament header and run it."""
    print(name)
    print_opponents(opponents)
    tournament(opponents)


def main() -> None:
    """Run the exercise 2 scenario."""
    run_named_tournament(
        "Tournament 0 (basic)",
        [
            (FlameFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
        ],
    )
    run_named_tournament(
        "Tournament 1 (error)",
        [
            (FlameFactory(), AggressiveStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
        ],
    )
    run_named_tournament(
        "Tournament 2 (multiple)",
        [
            (AquaFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy()),
        ],
    )


if __name__ == "__main__":
    main()
