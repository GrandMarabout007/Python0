class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, value: int) -> None:
        if value > 0:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, value: int) -> None:
        if value > 0:
            self.age = value
            print(f"Age updated: {value} days [OK]")
        else:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


def ft_garden_security():

    plant1 = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {plant1.name}")
    plant1.set_height(80)
    plant1.set_age(30)
    plant1.set_height(-9)


if __name__ == "__main__":
    print("=== Garden Security System ===")

    ft_garden_security()
