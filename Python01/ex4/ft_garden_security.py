class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Plant type with secured data, you can access it with get(),
      and edit it with set()

        Args:
            name (str): name of the created plant
            height (int): height of the plant in cm, must be > 0
            age (int): age of the plant, in days, must be > 0
        """
        self.set_name(name)
        self.__height = 0
        self.set_height(height)
        self.__age = 0
        self.set_age(age)

    def set_height(self, value: int) -> None:
        if value > 0:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, value: int) -> None:
        if value > 0:
            self.__age = value
            print(f"Age updated: {value} days [OK]")
        else:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_name(self) -> str:
        return self.__name

    def __repr__(self) -> str:
        return (f"Current plant: {self.__name} ({self.__height}cm, \
{self.__age} days)")


def ft_garden_security() -> None:

    plant1: 'SecurePlant' = SecurePlant("Rose", -25, 20)
    print(f"Plant created: {plant1.get_name()}")
    plant1.__height = 10
    plant1.set_height(6)
    print(plant1)


if __name__ == "__main__":
    print("=== Garden Security System ===")

    ft_garden_security()
