# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/11 14:18:43 by rschimme        #+#    #+#               #
#  Updated: 2026/02/16 18:01:09 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def inventory_master() -> None:
    """Your magical storage system where you can instantly find
    any item by name!
    """

    import sys
    inventory: dict = {}
    try:
        create_inventory(inventory)
    except ValueError:
        print(f"Error: Wrong input. Usage : python3 {sys.argv[0]} \
<item1:number> <item2:number> ...")
        return
    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique item types: {len(inventory)}")
    current_inventory(inventory)
    inventory_stats(inventory)
    abundance: dict[str, dict] = item_categories(inventory)
    management_suggestions(abundance)
    dict_demo(inventory)
    sample_lookup(inventory, "sword")
    sample_lookup(inventory, "stick")


def current_inventory(inventory: dict) -> None:
    """Prints the items in the inventory

    Args:
        inventory (dict): inventory
    """
    print("\n=== Current Inventory ===")
    total_items: int = sum(inventory.values())
    for item, value in inventory.items():
        print(f"{item}: {value} units ({((value/total_items) * 100):.1f}%)")


def item_categories(inventory: dict) -> dict:
    """splits the inventory in nested dicts, depending on their number

    Args:
        inventory (dict): inventory

    Returns:
        dict: the new dict, containing the rarity of items
    """
    print("\n=== Item Categories ===")
    abundance: dict[str, dict] = {
        "Common": {},
        "Moderate": {},
        "Scarce": {},
    }

    for item, value in inventory.items():
        if value <= 3:
            abundance["Scarce"][item] = value
        elif value < 10:
            abundance["Moderate"][item] = value
        else:
            abundance["Common"][item] = value
    for rarity, content in abundance.items():
        if len(content) != 0:
            print(f"{rarity}: {content}")
    return (abundance)


def management_suggestions(abundance: dict[str, dict]) -> None:
    """print the items that needs to be restocked or sold, depending
    on their number in the inventory

    Args:
        abundance (dict): dict that says if the item is rare or not
    """
    print("\n=== Management suggestions ===")
    if len(abundance["Scarce"]) > 0:
        print("Restock needed: ", end='')
        restock: 'list' = []
        for item in abundance["Scarce"]:
            restock.append(item)
        print(restock)
    if len(abundance["Common"]) > 0:
        print("Must be sold: ", end='')
        tosell: 'list' = []
        for item in abundance["Common"]:
            tosell.append(item)
        print(tosell)


def dict_demo(inventory: dict) -> None:
    """Shows the items and their number in the inventory

    Args:
        inventory (dict): _description_
    """
    print("\n=== Dictionary Properties Demo ===")
    keys: 'list' = []
    for key in inventory.keys():
        keys.append(key)
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {list(inventory.values())}")


def create_inventory(inventory: dict) -> None:
    """Parse throught the args, and create the inventory, a dict
    the items hsould be written this way <item:number>, else it will
    raise an error

    Args:
        inventory (dict): the empty inventory

    Raises:
        ValueError: if the input is not written the right way <item:number>

    Returns:
        _type_: the inventory, filled with the items and their number
    """
    import sys
    if len(sys.argv) == 1:
        raise ValueError
    for arg in sys.argv[1:]:
        if ':' in arg:
            arg_splitted = arg.split(':')
            if (arg_splitted[0] != '') and (int(arg_splitted[1]) > 0):
                inventory[arg_splitted[0]] = int(arg_splitted[1])
            else:
                raise ValueError
        else:
            raise ValueError
    return (inventory)


def inventory_stats(inventory: dict) -> None:
    """shows the most and least abundant iten in the inventory

    Args:
        inventory (dict): inventory
    """
    print("\n=== Inventory Statistics ===")
    most: 'str' = max(inventory, key=inventory.get)
    least: 'str' = min(inventory, key=inventory.get)
    print(f"Most abundant: {most} ({inventory[most]} units)")
    print(f"Least abundant: {least} ({inventory[least]} units)")


def sample_lookup(inventory: dict, sample: str):
    """Searches if the sample is in the inventory

    Args:
        inventory (dict): inventory
        sample (str): item to search
    """
    try:
        inventory[sample]
        print(f"Sample lookup - '{sample}' in inventory: True")
    except KeyError:
        print(f"Sample lookup - '{sample}' in inventory: False")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory_master()
