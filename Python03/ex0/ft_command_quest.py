# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 16:40:37 by rschimme        #+#    #+#               #
#  Updated: 2026/02/09 17:16:22 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def command_quest() -> None:
    """Print the name of the program, the number of arguments received
    as input, and print() them
    """
    import sys

    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        argnumber = 1
        for arg in sys.argv[1:]:
            print(f"Argument {argnumber}: {arg}")
            argnumber += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    command_quest()
