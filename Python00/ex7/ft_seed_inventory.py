def ft_seed_inventory(seed_type:	str, quantity:	int, unit:	str):
    seed_type = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{seed_type} seeds: {quantity} packets available")
    elif (unit == "area"):
        print(f"{seed_type} seeds: covers {quantity} square meters")
    elif (unit == "grams"):
        print(f"{seed_type} seeds: {quantity} grams total")
    else:
        print(f"{seed_type} seeds: {quantity} Unknown unit type")
