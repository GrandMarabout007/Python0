
from .elements import create_air, create_earth, create_fire, create_water


def healing_potion() -> str:
    return f"Healing potion breewed with {create_fire()} and {create_water()}"


def strengh_potion() -> str:
    return f"Strengh potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {create_air()} and {create_water()}"


def wisdom_potion() -> str:
    return f"Wisdom potion brewed with all elements: {create_water()} \
{create_air()} {create_fire()} {create_earth()}"
