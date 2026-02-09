# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/05 20:10:22 by rschimme        #+#    #+#               #
#  Updated: 2026/02/09 15:58:39 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def return_message(self) -> str:
        return (f"Caught {type(self).__name__} : {self.message}")


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def return_message(self) -> str:
        return super().return_message()


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def return_message(self) -> None:
        return super().return_message()


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        """Plant class, with a name, a water level and a sun level

        Args:
            name (str): Plant name
            water (int): Plant water level, between 1 and 10
            sun (int): Plant sunlight hours, between 2 and 12
        """
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    def __init__(self, name: str) -> None:
        """GardenManager is a class that contains methods to manage
        the garden, and raises Custom errors if needed.

        Args:
            name (str): Name of the manager
        """
        self.name = name
        self.garden = []

    def add_plants(self, tab: list) -> None:
        """Add plants to the garden. If the name of the plant is
        not valid, raises GardenError

        Args:
            tab (list): list of the plants to put in the garden

        Raises:
            GardenError: The specific error for the garden in general
        """
        print("Adding plants to garden...")
        for plant in tab:
            if plant.name is None:
                print("Error: Plant name cannot be empty !")
                raise GardenError("")
            else:
                self.garden.append(plant)
                print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        """Water the plants. if the plant name is not valid,
        raises WaterError, and close the watering system

        Raises:
            WaterError: The specific error for the water
        """
        print("Watering plants...")
        try:
            print("Opening the watering system")
            for plant in self.garden:
                if not isinstance(plant.name, str):
                    raise WaterError("")
                else:
                    print(f"Watering {plant.name}")
        except WaterError:
            print(f"Error: Cannot water {plant.name} - invalid plant!")
            raise WaterError("")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Checking the water and sunlight hours value. Raises a PlantError
        if the values are not correct
        Plant water level must be between 1 and 10
        Plant sunlight hours must be between 2 and 12

        Raises:
            PlantError: The specific error for the plants
        """
        for plant in self.garden:
            if plant.water < 1 or plant.water > 10:
                if plant.water > 10:
                    print(f"Error checking {plant.name}: Water level\
{plant.water} is too high (max 10)")
                elif plant.water < 1:
                    print(f"Error checking {plant.name}: Water level\
{plant.water} is too low (min 1)")
                raise PlantError("")
            if plant.sun < 2 or plant.sun > 12:
                if plant.sun > 12:
                    print(f"Error checking {plant.name}: Sunlight hours\
{plant.sun} is too high (max 12)")
                if plant.sun < 2:
                    print(f"Error checking {plant.name}: Sunlight hours\
{plant.sun} is too low (min 2)")
                raise PlantError("")
            print(f"Plant {plant.name} is healthy!")


def test_garden_management() -> None:
    tab: list = [
        ("tomato", 8, 6),
        ("rose", 15, 9),
        (None, 8, 3),
    ]
    tab2: list = []
    Manager = GardenManager("Manager")
    for infos in tab:
        newplant = Plant(*infos)
        tab2.append(newplant)
    try:
        Manager.add_plants(tab2)
    except GardenError:
        print("Caught: GardenError, but the program still runs")
    print()
    try:
        Manager.water_plants()
    except WaterError:
        print("Caught: WaterError, but the program still runs")
    finally:
        print()
    try:
        Manager.check_plant_health()
    except PlantError:
        print("Caught: PlantError, but the program still runs")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
