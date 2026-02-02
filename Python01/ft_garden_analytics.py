# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 17:41:32 by rschimme        #+#    #+#               #
#  Updated: 2026/02/02 20:04:00 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    plants = []
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
        self.plants.append(self)

    def grow(self, value: int) -> None:
        self.height = self.height + value

    def aging(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def week_simulate(self) -> int:
        for i in range(7):
            self.grow(self.growth_speed)
            self.aging()
        self.growth = (self.growth_speed * 7)

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, growth_speed: int, age: int, color: str, is_blooming: bool) -> None:
        super().__init__(name, height, age, growth_speed)
        self.color = color
        self.is_blooming = is_blooming
    
    def get_info(self) -> str:
        if self.is_blooming is True:
            return super().get_info() + f", {self.color} flowers (blooming)"
        else:
            return super().get_info() + f", {self.color} flowers (not blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, growth_speed: int, color: str, is_blooming: bool, prize_points: int) -> None:
        super().__init__(name, height, age, growth_speed, color, is_blooming)
        self.prize_points = prize_points

    def get_info(self) -> str:
        return super().get_info() + f", prize points : {self.prize_points}"


class GardenManager:
    main_garden = []

    def __init__(self, name):
        self.name = name
        self.gardens = {}

    def add_garden(self, gardener_name):
        if gardener_name not in self.gardens:
            self.gardens[gardener_name] = list()
            print(f"{gardener_name}'s garden created")
        else:
            print(f"{gardener_name}'s garden already exists")

    def add_flowers(self, gardener_name):
        for flower in self.main_garden:
            self.gardens[gardener_name].append(flower)
    # def add_garden(self, name)
    #     self.plants = []
    #     garden.append[self]


def ft_garden_analytics():
    
    Manager = GardenManager("Manager")
    gardeners = [
        ("Alice"),
        ("Fred"),
        ("Bob"),
        ("Alice"),
    ]
    flowers = [
        ("Rose", 25, 30, 1, "red", True),
        ("Sunflower", 80, 45, 2, "yellow", False),
        ("Nice Rose", 25, 30, 1, "red", True, 500),
        ("Shining Sunflower", 80, 45, 2, "yellow", False, 6200),
    ]
    for name in gardeners:
        Manager.add_garden(name)

    # for infos in flowers:
    #     new_flower = FloweringPlant(*infos)
    #     Manager.gardens["Alice"].append(new_flower)
    #     print(f"Added {new_flower.name} to Alice's garden")

    # for infos in prize_flowers:
    #     new_flower = PrizeFlower(*infos)
    #     Manager.garden.append(new_flower)
    #     print(f"Added {new_flower.name} to x garden")
    for infos in flowers:
        if len(infos) == 6:
            flower = FloweringPlant(*infos)
            Manager.main_garden.append(flower)
        elif len(infos) == 7:
            flower = PrizeFlower(*infos)
            Manager.main_garden.append(flower)
    
    Manager.add_flowers("Alice")
    for plant in Manager.gardens["Alice"]:
        print(plant.get_info())



if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    ft_garden_analytics()