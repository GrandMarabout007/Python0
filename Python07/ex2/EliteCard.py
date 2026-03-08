from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, total_mana):
        super().__init__(name, cost, rarity)
        self.damage = attack
        self.health = health
        self.total_mana = total_mana

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
        }

    def attack(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': 'melee',
        }

    def defend(self, incoming_damage: int):
        still_alive: bool = True
        if incoming_damage > self.health:
            still_alive = False
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.health,
            'still_alive': still_alive,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 2*len(targets)
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': self.total_mana,
        }

    def get_magic_stats(self) -> dict:
        return {
            'total_mana': self.total_mana
        }

    def get_combat_stats(self) -> dict:
        return {
            'Health': self.health,
            'Attack': self.damage,
        }
