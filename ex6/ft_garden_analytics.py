class Plant:
    _plist = []
    _total_increase: float = 0
    
    def __init__(self, name, height=0.0, days=0):
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
        self._calls = self.Stats()
    
    def grow(self, cm):
        self._height += cm
        Plant._total_increase += cm
        self._calls._grow_calls += 1
    
    def age(self, nb_days):
        self._days += nb_days
        self._calls._age_calls += 1
    
    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self._name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
    
    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_age
            print(f"Age updated: {new_age} days")
    
    def get_height(self):
        return self._height  
    
    def get_age(self):
        return self._days
    
    @staticmethod
    def check_age(nb):
        print(f"Is {nb} days more than a year -> {nb > 365}")
    
    @classmethod
    def anonymous(cls):
        return cls(name = "Unknown plant", days = 0, height = 0.0)
        
    def show(self):
        print(
            f"{self._name.capitalize()}: {round(self._height, 1)}cm, "
              f"{self._days} days old")
        self._calls._show_calls += 1
        
    class Stats:
        _grow_calls = 0
        _age_calls = 0
        _show_calls = 0

class Flower(Plant):
    def __init__(self, name, color, height=0, days=0):
        super().__init__(name, height, days)
        self._color: str = color
        self._blooming: bool = False
    
    def bloom(self):
        self._blooming = True
    
    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if  self._blooming:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")

class Seed(Flower):
    def __init__(self, name, color, height=0, days=0):
        super().__init__(name, color, height, days)
        self._seeds: int = 0
    
    def bloom(self):
        super().bloom()
        self._seeds = 42
    
    def show(self):
        super().show()
        print(f" Seeds: {self._seeds}")

class Tree(Plant):
    def __init__(self, name, trunk, height=0, days=0):
        super().__init__(name, height, days)
        self._trunk: float = trunk
        self._calls = self.TreeStats()
        self._shade: bool = False
    
    def produce_shade(self):
        self._shade = True
        print(
            f"Tree {self._name.capitalize()} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk, 1)}cm wide")
        self._calls._shade_calls += 1
    
    class TreeStats(Plant.Stats):
        _shade_calls = 0
    
    def show(self):
        super().show()
        print(f" Trunk Diameter: {round(self._trunk, 1)}cm")

class Vegetable(Plant):
    def __init__(self, name, harvest_season, height=0, days=0):
            super().__init__(name, height, days)
            self._harvest_season: str = harvest_season
            self._nutritional_value: int = 0
        
    def age(self):
        super().age()
        self._nutritional_value += 1
    
    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value}")

def plant_stats(plant_obj):
    print(
        f"Stats: {plant_obj._calls._grow_calls} grow, "
        f"{plant_obj._calls._age_calls} age, "
        f"{plant_obj._calls._show_calls} show")
    if isinstance(plant_obj, Tree):
        print(f" {plant_obj._calls._shade_calls} shade")

if __name__ == "__main__":
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    Plant.check_age(40)
    Plant.check_age(400)
    
    print("\n=== Flower")
    plant3 = Flower(
        name = "rose",
        height = 15.0,
        days = 10,
        color = "red")
    plant3.show()
    print("[statistics for Rose]")
    plant_stats(plant3)
    print("[asking the rose to grow and bloom]")
    plant3.grow(8.0)
    plant3.bloom()
    plant3.show()
    print("[statistics for Rose]")
    plant_stats(plant3)
    
    print("\n=== Tree")
    plant4 = Tree(
        name = "oak",
        height = 200,
        days = 365,
        trunk = 5.0
    )
    plant4.show()
    print("[statistics for Oak]")
    plant_stats(plant4)
    print("[asking the oak to produce shade]")
    plant4.produce_shade()
    print("[statistics for Oak]")
    plant_stats(plant4)

    print("\n=== Seed")
    plant2 = Seed(
        name = "Sunflower", 
        height = 80.0, 
        days = 45, 
        color = "yellow")
    plant2.show()
    print("[make the sunflower grow, age and bloom]")
    plant2.age(20)
    plant2.grow(30)
    plant2.bloom()
    plant2.show()
    print("[statistics for Sunflower]")
    plant_stats(plant2)

    print("\n=== Anonymous")
    plant1 = Plant.anonymous()
    plant1.show()
    print("[statistics for Unknown plant]")
    plant_stats(plant1)
    