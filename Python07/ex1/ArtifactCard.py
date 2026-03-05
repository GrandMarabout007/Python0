from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect
        self.type: str = "Artifact"
        self.in_play: bool = False

    def play(self, game_state: dict):
        self.in_play = True
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect,
        }

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            return {
                'effect': self.effect,
                'durability left': self.durability,
            }
        print("No more durability, cannot activate ability")
        return {
            'durability': 0
        }
