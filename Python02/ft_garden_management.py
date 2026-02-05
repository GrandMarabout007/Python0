# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/05 20:10:22 by rschimme        #+#    #+#               #
#  Updated: 2026/02/05 20:24:08 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name):
        self.name = name


class GardenManager:
    def __init__(self, name: str):
        self.name = name
        self.garden = []

    def add_plants(self, tab):
        for plant in tab:
            if plant.name is None:
                print("Error: Plant name cannot be empty !")
                raise ValueError
            self.garden.append(plant)
            print(f"Added {plant.name} successfully")


def test_garden_management():
    tab = [
        ("tomato"),
        ("rose"),
    ]
    tab2 = []
    Manager = GardenManager("Manager")
    for plant in tab:
        newplant = Plant(plant)
        tab2.append(newplant)

    Manager.add_plants(tab2)


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()