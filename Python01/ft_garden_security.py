class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, value):
        if value > 0:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Negative height rejected")
            
    def set_age(self, value):
        if value > 0:
            self.height = value
            print(f"Age updated: {value} days [OK]")
        else:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Negative age rejected")

    def get_height(self):
        return self.__height
       
    def get_age():
        return self.__age

def ft_garden_security():

    plant1 = SecurePlant("Rose", 25, 30)
    print(f"{plant1.name}")
    print(f"{plant1.get_height()}")
    plant1.set_height(80)
    print(f"{plant1.get_height()}")
    plant1.set_height(-9)
    print(f"{plant1.get_height()}")

if __name__ == "__main__":
    print("=== Garden Security System ===")

    ft_garden_security()