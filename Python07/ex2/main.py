from ex2.EliteCard import EliteCard


def main():
    aWarrior = EliteCard("Arcane Warrior", 6, "uncommon", 5, 3, 7)
    a = "Enemy"
    print(aWarrior.attack(a))
    print(aWarrior.defend(2))
    print(aWarrior.cast_spell('Fireball', ['goblin1', 'goblin2']))
    print(aWarrior.channel_mana(3))


if __name__ == "__main__":
    main()
