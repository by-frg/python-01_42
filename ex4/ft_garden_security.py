class Plant:
    _plist = []
    total_increase = 0
    
    def __init__(self, name, height=0, days=0):
        self._name: str = name
        
        if height >= 0:
            self._height: float = height
        else:
            self._height = 0
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
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
    
    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_age
            print(f"Age updated: {new_age} days")
    
    def get_height(self):
        return self._height  
    
    def get_age(self):
        return self._days
        
    def show(self):
        print(f"{self._name}: {round(self._height, 1)}cm, {self._days} days old")

if __name__ == "__main__":
    plant1 = Plant(
        name = "Rose",
        height = 0,
        days = 0
    )
    
    print("=== Garden Security System ===")
    print("Plant created: ", end=" ")
    plant1.show()
    print()
    
    plant1.set_age(30)
    plant1.set_height(25)
    print()
    
    plant1.set_age(-2)
    plant1.set_height(-3)
    print()
    
    print("Current state: ", end=" ")
    plant1.show()
    