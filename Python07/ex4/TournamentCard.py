from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard (Card, Combatable, Rankable):
	def __init__(self, name, cost, rarity):
		super().__init__(name, cost, rarity)
		self.id: str = None
		self.rating = 0
		self.victories = 0
		self.defeats = 0

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

	def calculate_rating(self) -> int:

	def get_tournament_stats(self) -> dict:
	


    def calculate_rating(self) -> int:

    def update_wins(self, wins: int) -> None:

    def update_losses(self, losses: int) -> None:

    def get_rank_info(self) -> dict:
