class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height = self.height + 1

    def aging(self):
        self.age += 1

    def get_info(self):
        return (self.name, self.height, self.age)


def ft_plant_growth():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Corn", 260, 63)
    plant3 = Plant("Wheat", 26, 32)
    print(f"{plant1.get_info()}")
    print(f"{plant2.get_info()}")
    for i in range(0, 7):
        plant1.grow()
        plant1.grow()
        plant1.aging()
    for i in range(1, 7):
        for j in range(0, 5):
            plant2.grow()
        plant2.aging()
    print(f"{plant1.get_info()}")
    print(f"{plant2.get_info()}")






    # def age()
if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_plant_growth()
