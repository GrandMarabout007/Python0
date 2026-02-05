# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/05 15:13:37 by rschimme        #+#    #+#               #
#  Updated: 2026/02/05 16:08:26 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

plant_list_error = [
      "tomato",
      "patrick",
      None,
      "carrot",
]

plant_list_clean = [
      "tomato",
      "patrick",
      "lettuce",
      "carrot",
]


def water_plants(plant_list):
    print("Opening the watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError()
            else:
                print(f"Watering {plant}")
    except ValueError:
        print(f"Error: Cannot water {plant} - invalid plant!")
        raise ValueError
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():

    try:
        print("Testing normal watering...")
        water_plants(plant_list_clean)
        print("Watering completed succesfully\n")
        print("Testing with error...")
        water_plants(plant_list_error)
    except ValueError:
        print("Caught: ValueError")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
