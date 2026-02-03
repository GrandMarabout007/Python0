def ft_garden_intro() -> None:
    """Print all plant's datas.

    Variables:
        name (str): plant name
        age (int): plant age, in days
        height (int): plant height, in cm
    """
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    ft_garden_intro()
    print('')
    print("=== End of Program ===")
