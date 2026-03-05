from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type
        self.type: str = "Spell"
        self.is_consumed = False

    def play(self, game_state: dict) -> dict:
        if self.is_consumed is False:
            self.is_consumed = True
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.effect_type,
            }
        else:
            print("spell already consumed")
            return None

    def resolve_effect(self, targets: list) -> dict:
        return {
            'effect': self.effect_type
        }
