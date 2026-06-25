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
    
    def grow(self, cm):
        self._height += cm
        Plant._total_increase += cm
    
    def age(self):
        self._days += 1
    
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

class Flower(Plant):
    _blooming: bool = False
    def __init__(self, name, color, height=0, days=0):
        super().__init__(name, height, days)
        self._color: str = color
    
    def bloom(self):
        self._blooming = True
        print(f"[asking the {self._name} to bloom]")
    
    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if  self._blooming:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")

class Tree(Plant):
    _shade: bool = False
    def __init__(self, name, trunk, height=0, days=0):
        super().__init__(name, height, days)
        self._trunk: float = trunk
    
    def produce_shade(self):
        self._shade = True
        print(f"asking the {self._name} to produce shade")
    
    def show(self):
        super().show()
        print(f" Trunk Diameter: {round(self._trunk, 1)}cm")
        if self._shade:
            print(
                f"Tree {self._name.capitalize()} now produces a shade of "
                f"{round(self._height, 1)}cm long and "
                f"{round(self._trunk, 1)}cm wide")
    
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

if __name__ == "__main__":
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    Plant.check_age(40)
    Plant.check_age(400)
    
    print("\n=== Anonymous")
    plant1 = Plant.anonymous()
    plant1.show()