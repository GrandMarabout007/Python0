from ex0.Card import Card
from typing import Any


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack: int = 0
        if attack >= 0:
            self.attack = attack
        self.health: int = 0
        if health >= 0:
            self.health = health
            self.type: str = "Creature"

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield',
        }

    def attack_target(self, target: Any) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True,
        }

    def get_card_info(self) -> dict:
        return super().get_card_info() | {"type": self.type,
                                          "attack": self.attack,
                                          "health": self.health}
