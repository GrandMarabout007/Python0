# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 15:48:40 by rschimme        #+#    #+#               #
#  Updated: 2026/02/03 17:11:51 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, age: int, gr_spe: int) -> None:
        """_summary_

        Args:
            name (str): Plant name
            height (int): Plant height, in cm
            age (int): Plant age, in days
            growth_speed (int): Plant growing speed, in cm per day
        """
        self.name = name
        self.height = height
        self.age = age
        self.growth_speed = gr_spe
        self.growth = 0

    def grow(self, value: int) -> None:
        self.height = self.height + value

    def aging(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def week_simulate(self) -> None:
        for i in range(7):
            self.grow(self.growth_speed)
            self.aging()
        self.growth = (self.growth_speed * 7)


def ft_plant_growth() -> None:
    plant1: 'Plant' = Plant("Rose", 25, 30, 1)
    plant2: 'Plant' = Plant("Corn", 260, 63, 6)

    print("=== Day 1 ===")
    print(plant1.get_info())
    print(plant2.get_info())
    plant1.week_simulate()
    plant2.week_simulate()
    print("=== Day 7 ===")
    print(plant1.get_info())
    print(plant2.get_info())
    print(f"{plant1.name} growth this week: +{plant1.growth}cm")
    print(f"{plant2.name} growth this week: +{plant2.growth}cm")
    plant1.growth = 0
    plant2.growth = 0


if __name__ == "__main__":
    ft_plant_growth()
