# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/11 14:18:43 by rschimme        #+#    #+#               #
#  Updated: 2026/02/11 16:26:16 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def inventory_master():

    inventory = {}
    import sys
    for arg in sys.argv[1:]:
        try:
            if ':' in arg:
                arg_splitted = arg.split(':')
                if arg_splitted[0] != '':
                    inventory[arg_splitted[0]] = int(arg_splitted[1])
                else: 
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print(f"Error: Wrong input. Usage : python3 {sys.argv[0]} \
<item1:number> <item2:number> ...")
            return ()
    print(inventory)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory_master()
