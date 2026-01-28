# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 15:48:40 by rschimme        #+#    #+#               #
#  Updated: 2026/01/27 15:50:36 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = self.height + 1

    def aging(self) -> None:
        self.age += 1

    def get_info(self) -> tuple[str, int, int]:
        return self.name, self.height, self.age


def ft_plant_growth():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Corn", 260, 63)
    name1, height1, age1 = plant1.get_info()
    name2, height2, age2 = plant2.get_info()
    print("=== Day 1 ===")
    print(f"{name1}: {height1}cm, {age1} days old")
    print(f"{name2}: {height2}cm, {age2} days old")
    for i in range(0, 7):
        plant1.grow()
        plant1.grow()
        plant1.aging()
    for i in range(1, 7):
        for i in range(0, 5):
            plant2.grow()
        plant2.aging()
    print("=== Day 7 ===")
    growth = plant1.height - height1
    growth2 = plant2.height - height2
    name1, height1, age1 = plant1.get_info()
    name2, height2, age2 = plant2.get_info()
    print(f"{name1}: {height1}cm, {age1} days old")
    print(f"{name2}: {height2}cm, {age2} days old")
    print(f"{name1} growth this week: +{growth}cm")
    print(f"{name2} growth this week: +{growth2}cm")


if __name__ == "__main__":
    ft_plant_growth()
