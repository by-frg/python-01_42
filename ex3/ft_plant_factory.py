class Plant:
    total_increase = 0
    plist = []
    
    def __init__(self, name, height, days):
        self.name: str = name
        self.height: float = height
        self.days: int = days
        Plant.plist.append(self)
    
    def grow(self, cm):
        self.height += cm
        Plant.total_increase += cm
    
    def age(self):
        self.days += 1
        
    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

if __name__ == "__main__":
    plant1 = Plant(
        name = "Rose",
        height = 25,
        days = 30
    )

    plant2 = Plant(
        name = "Oak",
        height = 200,
        days = 365
    )

    plant3 = Plant(
        name = "Cactus",
        height = 5,
        days = 90
    )

    plant4 = Plant(
        name = "Sunflower",
        height = 80,
        days = 45
    )

    plant5 = Plant(
        name = "Fern",
        height = 15,
        days = 120
    )
    
    print("=== Plant Factory Output ===")
    for x in Plant.plist:
        print("Created:", end=" ")
        x.show()
