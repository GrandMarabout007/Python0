
def check_plant_health(plant_name, water_level, sunlight_hours) -> str:

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


def test_plant_checks():
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
