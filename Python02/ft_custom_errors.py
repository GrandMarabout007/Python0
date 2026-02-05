# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 19:17:45 by rschimme        #+#    #+#               #
#  Updated: 2026/02/05 15:12:42 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str):
        self.message = message

    def return_message(self) -> str:
        return (f"Caught {type(self).__name__} : {self.message}")


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)

    def return_message(self):
        return super().return_message()


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)

    def return_message(self):
        return super().return_message()


def custom_error_1by1():

    error_garden = GardenError("The garden is full of bugs")
    error_plant = PlantError("The tomato plant is wilting !")
    error_water = WaterError("The water is dirty")

    print("Testing GardenError...")
    try:
        raise error_garden
    except GardenError:
        print(f"{error_garden.return_message()}\n")
    print("Testing PlantError...")
    try:
        raise error_plant
    except PlantError:
        print(f"{error_plant.return_message()}\n")
    print("Testing WaterError...")
    try:
        raise error_water
    except WaterError:
        print(f"{error_water.return_message()}\n")


def custom_error_multiple():
    errors = [
        GardenError("The garden is full of bugs"),
        WaterError("The water tank is almost empty"),
        WaterError("The water is dirty"),
        PlantError("The tomato plant is wilting !"),
    ]
    print("Testing catching all garden errors...")
    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"{e.return_message()}")

    print("\nTesting catching all water errors...")
    for error in errors:
        try:
            raise error
        except WaterError as e:
            print(f"{e.return_message()}")
        except GardenError:
            print("Not a WaterError, but the program is still running")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    custom_error_1by1()
    custom_error_multiple()
