import random
from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        if self.cards:
            self.cards.remove(card_name)
            return True
        print("error, no more cards to draw")
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            print(f'Drew: {self.cards[0].name} ({self.cards[0].type})')
            return self.cards.pop(0)
        print("error, no more cards to draw")
        return None

    def get_deck_stats(self) -> dict:
        total_cost: int = 0
        total_creatures: int = 0
        total_spells: int = 0
        total_artifacts: int = 0

        for card in self.cards:
            total_cost += card.cost
            if card.type == 'Creature':
                total_creatures += 1
            elif card.type == 'Spell':
                total_spells += 1
            elif card.type == 'Artifact':
                total_artifacts += 1
        avg_cost: float = round(total_cost/len(self.cards), 1)
        return {
            'total_cards': len(self.cards),
            'creatures': total_creatures,
            'spells': total_spells,
            'artifacts': total_artifacts,
            'avg_cost': avg_cost,
        }
