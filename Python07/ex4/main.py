
from ex0.CreatureCard import CreatureCard


registered = {}
def register_card(card: CreatureCard) -> str:
    count = 1
    while True:
        new_id = f"{card.name}_{count:03d}"
        if new_id not in registered:
            break
        count += 1
    registered[new_id] = card
    return new_id


def main():

    print("\n === DataDeck Tournament Platform ===\n")

    card1 = CreatureCard("psy", 5, 9, 1, 3)
    card2 = CreatureCard("oui", 5, 9, 1, 3)
    card3 = CreatureCard("psy", 5, 9, 1, 3)
    card4 = CreatureCard("oui", 5, 9, 1, 3)
    card5 = CreatureCard("psy", 5, 9, 1, 3)

    print(register_card(card1))
    print(register_card(card2))
    print(register_card(card3))
    print(register_card(card4))
    print(register_card(card5))


if __name__ == "__main__":
    main()
