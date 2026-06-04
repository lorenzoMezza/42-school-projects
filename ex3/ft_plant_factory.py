#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.days_old = age
        self.growth_rate = 1.0

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        height = round(self.height, 1)
        print(f"{self.name}: {height}cm, {self.days_old} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", end=" ")
        plant.show()
