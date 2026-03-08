from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


def main():

    print("\n=== DataDeck Deck Builder ===\n")

    game_state: dict = {}

    L_bolt = SpellCard("Lightning Bolt", 3, "common", "Deal 3 damage to target\
")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "uncommon", 6,
                                "Permanent: +1 mana per turn")
    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)

    main_deck = Deck()
    main_deck.add_card(L_bolt)
    main_deck.add_card(mana_crystal)
    main_deck.add_card(dragon)
    print("Building deck with different card types...")
    print(main_deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")
    for i in range(3):
        drawed = main_deck.draw_card()
        print("Play result:", drawed.play(game_state), '\n')


if __name__ == "__main__":
    main()
