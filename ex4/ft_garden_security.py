#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = 1.0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = float(height)
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        height = round(self._height, 1)
        print(f"{self.name}: {height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()

    if rose.set_height(25):
        print("Height updated: 25cm")
    else:
        print("Height update rejected")

    if rose.set_age(30):
        print("Age updated: 30 days")
    else:
        print("Age update rejected")

    if rose.set_height(-5):
        print("Height updated: -5cm")
    else:
        print("Height update rejected")

    if rose.set_age(-10):
        print("Age updated: -10 days")
    else:
        print("Age update rejected")

    print("Current state:", end=" ")
    rose.show()
