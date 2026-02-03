# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 16:08:31 by rschimme        #+#    #+#               #
#  Updated: 2026/02/03 17:15:25 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return (f"{self.name} ({type(self).__name__}): {self.height}cm,\
 {self.age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming !\n")

    def get_info(self):
        return super().get_info() + f", {self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.trunk_diameter * 1.3} \
square meters of shade\n")

    def get_info(self):
        return super().get_info() + f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return super().get_info() + f", {self.harvest_season} harvest"


def ft_plant_types() -> None:

    flowers = [
        ("Rose", 25, 30, "red"),
        ("Sunflower", 80, 45, "yellow"),
    ]

    trees = [
        ("Oak", 200, 365, 35),
        ("Pine", 15, 120, 17),
    ]

    vegetables = [
        ("Tomato", 9, 45, "summer", "vitamin C"),
        ("Parsnip", 47, 60, "fall", "vitamin E"),
        ("Beetroot", 16, 27, "summer", "vitamin A"),
    ]
    garden = []

    for name_x, height_y, age_z, color_c in flowers:
        new_flower: 'Flower' = Flower(name_x, height_y, age_z, color_c)
        garden.append(new_flower)

    for name_x, height_y, age_z, trunk_t in trees:
        new_tree: 'Tree' = Tree(name_x, height_y, age_z, trunk_t)
        garden.append(new_tree)

    for name_x, height_y, age_z, harvest_s, nutri_v in vegetables:
        new_vegetable: 'Vegetable' = Vegetable(name_x, height_y, age_z, harvest_s, nutri_v)
        garden.append(new_vegetable)

    for plant in garden:
        print(f"{plant.get_info()}")
        match plant:
            case Flower():
                plant.bloom()
            case Tree():
                plant.produce_shade()
            case Vegetable(nutritional_value=v):
                print(f"{plant.name} is rich in {v}\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    ft_plant_types()
