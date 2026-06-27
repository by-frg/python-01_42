class Plant:
    _plist: list["Plant"] = []
    _total_increase: float = 0

    def __init__(self, name: str, height: float = 0.0, days: int = 0) -> None:
        self._name: str = name
        if height >= 0:
            self._height: float = float(height)
        else:
            self._height = 0.0
        if days >= 0:
            self._days: int = days
        else:
            self._days = 0
        Plant._plist.append(self)

    def grow(self, cm: float) -> None:
        self._height += cm
        Plant._total_increase += cm

    def age(self) -> None:
        self._days += 1

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(
                f"{self._name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_age
            print(f"Age updated: {new_age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: {round(self._height, 1)}cm, "
            f"{self._days} days old")


class Flower(Plant):
    def __init__(self, name: str, color: str,
                 height: float = 0, days: int = 0):
        super().__init__(name, height, days)
        self._color: str = color
        self._blooming: bool = False

    def bloom(self) -> None:
        self._blooming = True
        print(f"[asking the {self._name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, trunk: float,
                 height: float = 0.0, days: int = 0) -> None:
        super().__init__(name, height, days)
        self._trunk: float = trunk
        self._shade: bool = False

    def produce_shade(self) -> None:
        self._shade = True
        print(f"asking the {self._name} to produce shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {round(self._trunk, 1)}cm")
        if self._shade:
            print(
                f"Tree {self._name.capitalize()} now produces a shade of "
                f"{round(self._height, 1)}cm long and "
                f"{round(self._trunk, 1)}cm wide")


class Vegetable(Plant):
    def __init__(self, name: str, harvest_season: str,
                 height: float = 0.0, days: int = 0):
        super().__init__(name, height, days)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    plant1 = Flower(
        name="rose",
        height=15,
        days=10,
        color="red"
    )
    plant2 = Tree(
        name="oak",
        height=200,
        days=365,
        trunk=5
    )
    plant3 = Vegetable(
        name="tomato",
        height=5,
        days=10,
        harvest_season="april"
    )

    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1.show()
    plant1.bloom()
    plant1.show()
    print("\n=== Tree")
    plant2.show()
    plant2.produce_shade()
    plant2.show()
    print("\n=== Vegetable")
    plant3.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        plant3.grow(2.1)
        plant3.age()
    plant3.show()
