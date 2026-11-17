#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.days_old = age
        self.growth_rate = 0.8

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        height = round(self.height, 1)
        print(f"{self.name}: {height}cm, {self.days_old} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    start_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    total_growth = round(rose.height - start_height, 1)
    print(f"Growth this week: {total_growth}cm")
