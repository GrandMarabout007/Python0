class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Plant type, that can print itself via __repr__

        Args:
            name (str): Plant name
            height (int): Plant height, in cm
            age (int): Plant age, in days
        """
        self.name = name
        self.height = height
        self.age = age

    def __repr__(self) -> str:
        return (f"{self.name}: ({self.height}cm, {self.age} days)")


def ft_garden_data() -> None:
    """create plants and print them
    """

    plant1: 'Plant' = Plant("Corn", 260, 63)
    plant2: 'Plant' = Plant("Wheat", 26, 32)
    plant3: 'Plant' = Plant("Cactus", 15, 120)
    print(plant1)
    print(plant2)
    print(plant3)


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
