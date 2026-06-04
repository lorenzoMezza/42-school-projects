#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self._growth_rate = 1.0
        self._stats = Plant.Stats()
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> Stats:
        return self._stats

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def grow(self) -> None:
        self._height += self._growth_rate
        self._stats.add_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.add_age()

    def show(self) -> None:
        self._stats.add_show()
        height = round(self._height, 1)
        print(f"{self.name}: {height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False
        self._growth_rate = 8.0

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self._stats = Tree.TreeStats()
        self.trunk_diameter = trunk_diameter

    def get_stats(self) -> TreeStats:
        return self._stats

    def produce_shade(self) -> None:
        self._stats.add_shade()
        height = round(self.get_height(), 1)
        diameter = round(self.trunk_diameter, 1)
        print(
            f"Tree {self.name} now produces a shade of "
            f"{height}cm long and {diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        diameter = round(self.trunk_diameter, 1)
        print(f"Trunk diameter: {diameter}cm")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0
        self._growth_rate = 30.0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def age(self) -> None:
        self._age += 20
        self.get_stats().add_age()

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    result = Plant.is_older_than_a_year(30)
    print(f"Is 30 days more than a year? -> {result}")
    result = Plant.is_older_than_a_year(400)
    print(f"Is 400 days more than a year? -> {result}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)
