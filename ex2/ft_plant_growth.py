class Plant:
    total_increase = 0
    
    def __init__(self):
        self.name: str = ""
        self.height: float = ""
        self.days: int = ""
    
    def grow(self, cm):
        self.height += cm
        Plant.total_increase += cm
    
    def age(self):
        self.days += 1
        
    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

if __name__ == "__main__":
    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 25
    plant1.days = 30
       
    print("=== Garden Plant Growth ===")
    plant1.show()
    for i in range(1, 8):
        plant1.grow(0.8)
        plant1.age()
        print(f"=== Day {i} ===")
        plant1.show()
    print(f"Growth this week: {plant1.total_increase}")
        