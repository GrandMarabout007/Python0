# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_errors.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rschimme <rschimme@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 16:09:11 by rschimme          #+#    #+#              #
#    Updated: 2026/02/05 20:04:51 by rschimme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str):
        self.message = message

    def return_message(self) -> str:
        return (f"Caught {type(self).__name__} : {self.message}")


class SunlighError(GardenError):
    def __init__(self, message):
        super().__init__(message)

    def return_message(self):
        return super().return_message()


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)

    def return_message(self):
        return super().return_message()

class PlantnameError(GardenError):
    def __init__(self, message):
        super().__init__(message)

    def return_message(self):
        return super().return_message()


def check_plant_health(plant_name, water_level, sunlight_hours) -> str:

    if plant_name is None:
        print("Error: Plant name cannot be empty !")
        raise ValueError
    if water_level < 1 or water_level > 10:
        if water_level > 10:
            print(f"Error: Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            print(f"Error: Water level {water_level} is too low (min 1)")
        raise WaterError("")
    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours > 12:
            print(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
        if sunlight_hours < 2:
            print(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
        raise SunlighError("")
    return (f"Plant {plant_name} is healthy!")


def test_plant_checks():
    print("Testing good values...")
    try:
        print(check_plant_health("Rose", 8, 8))
    except (ValueError, WaterError, SunlighError):
        raise ValueError
    print("Testing empty plant name...")
    try:
        try:
            print(check_plant_health(None, 8, 8))
        except (PlantnameError, WaterError, SunlighError):
            raise ValueError
        print("Testing bad water level...")
        try:
            print(check_plant_health("Rose", 26, 8))
        except (PlantnameError, WaterError, SunlighError):
            raise ValueError
        print("Testing bad sunlight hours...")
        try:
            print(check_plant_health("Rose", 8, 23))
        except (PlantnameError, WaterError, SunlighError):
            raise ValueError
    except ValueError:
        print ("ValueError raised, but tests completed")





if __name__ == "__main__":
    test_plant_checks()