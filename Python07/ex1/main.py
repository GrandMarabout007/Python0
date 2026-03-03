# from .ex0.Card import Card
from Card import Card
from CreatureCard import CreatureCard
import random
# from General Instructions import enum


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type,
        }

    def resolve_effect(self, targets: list) -> dict:
        pass


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: dict):
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect,
        }

    def activate_ability(self) -> dict:
        pass

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        self.cards.remove(card_name)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        print("Drew: ", end="")
        return (self.cards(0))

    def get_deck_stats(self) -> dict:
        return(self.cards)


def main():
    game_state: dict = {}
    L_bolt = SpellCard("Lightning Bolt", 3, "common", "Deal 3 damage to target")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "uncommon", 98, "Permanent: +1 mana per turn")
    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    main_deck = Deck()
    main_deck.add_card(L_bolt)
    main_deck.add_card(mana_crystal)
    main_deck.add_card(dragon)
    for card in main_deck.cards:
        print(card.play(game_state))
    main_deck.shuffle()
    print()
    for card in main_deck.cards:
        print(card.play(game_state))


if __name__ == "__main__":
    main()