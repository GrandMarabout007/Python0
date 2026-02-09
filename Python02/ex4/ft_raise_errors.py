
def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Checking the water and sunlight hours value. Raises a ValueError
        if the values are not correct
        Plant water level must be between 1 and 10
        Plant sunlight hours must be between 2 and 12

    Args:
        plant_name (str): plant name
        water_level (int): water level, must be between 1 and 10
        sunlight_hours (int): sunlight hours, must be between 2 and 12

    Raises:
        ValueError: Raised if the water_level or the sunlight_hours
        are not in their range

    Returns:
        str: Succes message if everything is okay
    """
    if plant_name is None:
        print("Error: Plant name cannot be empty !")
        raise ValueError
    if water_level < 1 or water_level > 10:
        if water_level > 10:
            print(f"Error: Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            print(f"Error: Water level {water_level} is too low (min 1)")
        raise ValueError
    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours > 12:
            print(f"Error: Sunlight hours {sunlight_hours} is too \
high (max 12)")
        if sunlight_hours < 2:
            print(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
        raise ValueError
    return (f"Plant {plant_name} is healthy!")


def test_plant_checks() -> None:
    """Tests all cases of error
    """
    print("Testing good values...")
    print(check_plant_health("Rose", 8, 8), "\n")
    print("Testing empty plant name...")
    try:
        print(check_plant_health(None, 8, 8))
    except ValueError:
        print("ValueError raised, but tests continues\n")
    print("Testing bad water level...")
    try:
        print(check_plant_health("Rose", 26, 8))
    except ValueError:
        print("ValueError raised, but tests continues\n")
    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("Rose", 8, 23))
    except ValueError:
        print("ValueError raised, but tests continues\n")
    print("All error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
