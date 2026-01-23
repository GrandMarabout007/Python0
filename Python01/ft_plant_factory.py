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
        return self.name, self.height, self.age


def ft_plant_factory():
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    garden = []

    for name_x, height_y, age_z in plants:
        new_plant = Plant(name_x, height_y, age_z)
        garden.append(new_plant)

    total = 0
    for plant in garden:
        x, y, z = plant.get_info()
        print(f"Created: {x} ({y}cm, {z} days)")
        total = total + 1
    print(f"Total plants created: {total}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    ft_plant_factory()
