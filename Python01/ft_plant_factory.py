class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = self.height + 1

    def aging(self) -> None:
        self.age += 1

    def get_info(self) -> tuple[str, int, int]:
        return self.name, self.height, self.age

    def __repr__(self) -> str:
        return (f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory() -> None:
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

    # for infos in plants:
    #     new_plant = Plant(*infos)
    total = 0
    for plant in garden:
        print(plant)
        total = total + 1
    print(f"Total plants created: {total}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    ft_plant_factory()
