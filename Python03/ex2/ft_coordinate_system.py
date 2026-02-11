# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 18:15:56 by rschimme        #+#    #+#               #
#  Updated: 2026/02/10 15:06:38 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_coordinates_system() -> None:

    origin: tuple = (0, 0, 0)
    pos1: tuple = (10, 20, 5)
    print(f"Position created: {pos1}")
    dist(pos1, origin)
    pos2 = (parsing_coordinates("8,9,2"))
    dist(pos2, origin)
    pos3 = (parsing_coordinates("8,9a,2"))
    dist(pos3, origin)
    print()
    unpacking_magic(pos2)


def dist(pos1: tuple, pos2: tuple) -> None:
    import math
    if (pos1 and pos2) is not None:
        distance = (math.sqrt(((pos1[0]-pos2[0])**2)
                    + ((pos1[1]-pos2[1])**2) + ((pos1[2]-pos2[2])**2)))
        print(f"Distance between {pos1} and {pos2}: {distance:.2f}\n")


def parsing_coordinates(input: str) -> tuple:
    print(f"Parsing coordinates: \"{input}\"")
    x = input.split(",")
    try:
        pos = (int(x[0]), int(x[1]), int(x[2]))
        print(f"Parsed position: {pos}")
        return (pos)
    except ValueError:
        print("Error, Error parsing coordinates: invalid literal for int() \
with base 10")


def unpacking_magic(pos: tuple) -> None:
    print("Unpacking demonstration:")
    if pos is not None:
        print(f"Player at x={pos[0]}, y={pos[1]}, z={pos[2]}")
        print(f"Coordinates: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    ft_coordinates_system()
