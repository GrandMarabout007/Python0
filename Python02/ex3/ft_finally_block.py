# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/05 15:13:37 by rschimme        #+#    #+#               #
#  Updated: 2026/02/09 18:33:15 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

plant_list_error: list = [
      "tomato",
      "patrick",
      None,
      "carrot",
]

plant_list_clean: list = [
      "tomato",
      "patrick",
      "lettuce",
      "carrot",
]


def water_plants(plant_list: list) -> None:
    """Water the plants. if the plant name is not valid,
        raises ValueError, and close the watering system

    Args:
        plant_list (list): list of the plants to water

    Raises:
        ValueError: raised if the plant name is not valid
    """
    try:
        print("Opening the watering system")
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


def test_watering_system() -> None:
    """demonstrates normal watering with a good plant list,
    watering with a bad plant list, and that cleanup always happens
    """

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
