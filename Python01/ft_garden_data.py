class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():

    plant1 = Plant("Corn", 260, 63)
    plant2 = Plant("Wheat", 26, 32)
    plant3 = Plant("Cactus", 15, 120)
    print(plant1.name, ":", plant1.height, "cm,", plant1.age, "days old")
    print(plant2.name, ":", plant2.height, "cm,", plant2.age, "days old")
    print(plant3.name, ":", plant3.height, "cm,", plant3.age, "days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
