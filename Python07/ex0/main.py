from ex0.CreatureCard import CreatureCard


def main():

    print("\n=== DataDeck Card Foundation ===\n")
    game_state: dict = {}
    Creature_1: dict = {
        "name": 'Fire Dragon',
        "cost": 5,
        'rarity': 'Legendary',
        'attack': 7,
        'health': 5,
    }
    dragon = CreatureCard(Creature_1['name'], Creature_1['cost'],
                          Creature_1['rarity'], Creature_1['attack'],
                          Creature_1['health'])
    print("CreatureCard Info:")
    print(dragon.get_card_info(), "\n")

    print(f"Playing {dragon.name} with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    game_state = dragon.play(game_state)
    print(game_state, '\n')

    print(f"{dragon.name} attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("Abstract pattern succesfully demonstrated!")


if __name__ == "__main__":
    main()
