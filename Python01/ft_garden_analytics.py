# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 17:41:32 by rschimme        #+#    #+#               #
#  Updated: 2026/01/28 20:20:14 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
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
    
    def grow(self, value) -> None:
        self.__height = self.__height + value
        print(f"{self.name} grew {value}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, prize: int) -> None:
        super().__init__(name, height, age, color)
        self.prize = prize



class GardenManager():
    def __init__(self, gardens: int, gardener: str)
        
    def create_garden_network()
        
    class GardenStats()
        



def ft_plant_types() -> None:

    flowers = [
        ("Rose", 25, 30, "red"),
        ("Sunflower", 80, 45, "yellow"),
    ]
    Gardeners = [
        ("Alice"),
        ("Fred"),
    ]

    trees = [
        ("Oak", 200, 365),
        ("Pine", 15, 120, 17),
    ]

    garden = []

    for infos in flowers:
        new_flower = FloweringPlant(*infos)
        garden.append(new_flower)
        print(f"Added {plant.name} to ")


#     for plant in garden:
#         base_plant = f"{plant.name} ({type(plant).__name__}): \
# {plant.height}cm, {plant.age} days, "

#         match plant:
#             case Flower(color=c):
#                 special_info = (f"{c} color")
#                 print(base_plant + special_info)
#                 plant.bloom()
#             case Tree(trunk_diameter=d):
#                 special_info = f"{d}cm diameter"
#                 print((base_plant + special_info))
#                 plant.produce_shade()
#             case _:
#                 print(base_plant)


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    ft_plant_types()