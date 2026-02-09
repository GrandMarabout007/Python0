# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 17:41:32 by rschimme        #+#    #+#               #
#  Updated: 2026/02/09 15:40:50 by rschimme        ###   ########.fr        #
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
        self.set_name(name)
        self.__height = 0
        self.set_height(height)
        self.__age = 0
        self.set_age(age)
        self.growth_speed = gr_spe
        self.growth = 0

    def grow(self, value: int) -> None:
        self.__height = self.__height + value

    def aging(self) -> None:
        self.__age += 1

    def get_info(self) -> str:
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"

    def set_height(self, value: int) -> None:
        if value > 0:
            self.__height = value
            # print(f"Height updated: {value}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, value: int) -> None:
        if value > 0:
            self.__age = value
            # print(f"Age updated: {value} days [OK]")
        else:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_name(self) -> str:
        return self.__name


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, growth_speed: int,
                 color: str, is_blooming: bool) -> None:
        super().__init__(name, height, age, growth_speed)
        self.color = color
        self.is_blooming = is_blooming

    def get_info(self) -> str:
        if self.is_blooming is True:
            return super().get_info() + f", {self.color} flowers (blooming)"
        else:
            return super().get_info() + f", {self.color} flowers \
(not blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, growth_speed: int,
                 color: str, is_blooming: bool, prize_points: int) -> None:
        super().__init__(name, height, age, growth_speed, color, is_blooming)
        self.prize_points = prize_points

    def get_info(self) -> str:
        return super().get_info() + f", Prize points : {self.prize_points}"


class GardenManager:
    temp_garden = []

    def __init__(self, name):
        self.name = name
        self.gardens = {}
        self.points = {}

    def create_garden_network(self, gardener_name: str) -> None:
        if gardener_name not in self.gardens:
            self.gardens[gardener_name] = list()
            print(f"{gardener_name}'s garden created")
        else:
            print(f"{gardener_name}'s garden already exists")

    def add_flowers(self, gardener_name: str) -> None:
        for plant in self.temp_garden:
            self.gardens[gardener_name].append(plant)
            print(f"Added {plant.get_name()} to {gardener_name}'s garden")
        self.temp_garden = []
        print()

    def week_simulate(self) -> int:
        for gardener in self.gardens:
            if self.gardens[gardener]:
                print(f"{gardener} is helping all plants grow..")
                for plant in self.gardens[gardener]:
                    for i in range(7):
                        plant.grow(plant.growth_speed)
                        plant.aging()
                    plant.growth = (plant.growth_speed * 7)
                    print(f"{plant.get_name()} grew {plant.growth}cm \
this week")
                    plant.growth = 0
                print()

    def print_garden_report(self) -> None:
        for gardener in self.gardens:
            print(f"=== {gardener}'s Garden Report ===")
            if self.gardens[gardener]:
                print("Plants in garden:")
                regular = 0
                flowering = 0
                prize = 0
                for plant in self.gardens[gardener]:
                    if isinstance(plant, PrizeFlower):
                        prize += 1
                    elif isinstance(plant, FloweringPlant):
                        flowering += 1
                    elif isinstance(plant, Plant):
                        regular += 1
                    print(f"{plant.get_info()}")
                print(f"Plants added: {prize + flowering + regular}")
                print(f"Plant types: {regular} regular, {flowering} \
flowering, {prize} prize flowers\n")
            else:
                print("No plants in garden\n")

    def count_gardens(self) -> None:
        total = 0
        for gardeners in self.gardens:
            total = total + 1
        print(f"Total gardens managed: : {total}")

    class GardenStats:
        def calculate_points(self) -> None:
            for gardener in self.gardens:
                total = 0
                if self.gardens[gardener]:
                    for plant in self.gardens[gardener]:
                        if isinstance(plant, PrizeFlower):
                            total += plant.prize_points
                        if isinstance(plant, FloweringPlant):
                            total += 50
                            if plant.is_blooming is True:
                                total += 200
                        if isinstance(plant, Plant):
                            total += plant.get_height()
                    self.points[gardener] = total

        def print_scores(self) -> None:
            print("Garden scores -", end='')
            for gardener in self.gardens:
                if gardener in self.points:
                    print(f" {gardener}: {self.points[gardener]}", end='')
                else:
                    print(f" {gardener}: 0", end='')
            print()


def ft_garden_analytics():

    Manager = GardenManager("Manager")
    gardeners = [
        ("Alice"),
        ("Fred"),
        ("Bob"),
        ("Alice"),
    ]
    plants = [
        ("Rose", 25, 30, 1, "red", True),
        ("Sunflower", 80, 45, 2, "yellow", False),
        ("Nice Rose", 25, 30, 1, "red", True, 300),
        ("Shining Sunflower", 80, 45, 2, "yellow", False, 1200),
    ]
    print("=== Creating gardens ===")
    for name in gardeners:
        Manager.create_garden_network(name)
    print()

    for infos in plants:
        if len(infos) == 4:
            newplant: 'Plant' = Plant(*infos)
        elif len(infos) == 6:
            newplant: 'FloweringPlant' = FloweringPlant(*infos)
        elif len(infos) == 7:
            newplant: 'PrizeFlower' = PrizeFlower(*infos)
        Manager.temp_garden.append(newplant)

    Manager.add_flowers("Alice")
    plants_2 = [
        ("Oak Tree", 250, 360, 4),
        ("Blue Edelweiss", 8, 120, 1, "blue", True, 11000),
        ("Tomato flower", 60, 2, 3, "white", True),
    ]
    for infos in plants_2:
        if len(infos) == 4:
            newplant: 'Plant' = Plant(*infos)
        elif len(infos) == 6:
            newplant: 'FloweringPlant' = FloweringPlant(*infos)
        elif len(infos) == 7:
            newplant: 'PrizeFlower' = PrizeFlower(*infos)
        Manager.temp_garden.append(newplant)

    Manager.add_flowers("Bob")
    Manager.print_garden_report()
    Manager.week_simulate()
    GardenManager.GardenStats.calculate_points(Manager)
    GardenManager.GardenStats.print_scores(Manager)
    GardenManager.count_gardens(Manager)


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    ft_garden_analytics()
