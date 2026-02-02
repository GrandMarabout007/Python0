class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Plant type,
        You can get the data with get_info(), and print it via __repr__

        Args:
            name (str): Plant age
            height (int): Plant height, in cm
            age (int): Plant age, in days
        """
        self.name = name
        self.height = height
        self.age = age

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

    total = 0
    for plant in garden:
        print(plant)
        total = total + 1
    print(f"Total plants created: {total}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    ft_plant_factory()
