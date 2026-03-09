from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy (GameStrategy):
    def __init__(self):
        self.strat_name = 'Aggressive'

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_used: int = 0
        if not hand:
            raise ValueError
        if not battlefield:
            battlefield = 'No targets'
        for card in hand:
            if isinstance(card, Card):
                mana_used += card.cost
            else:
                raise ValueError
        cards_played: list = []
        for card in hand:
            cards_played.append(card.name)

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': battlefield
        }

    def get_strategy_name(self) -> str:
        return self.strat_name

    def prioritize_targets(self, available_targets: list) -> list:
        prio: list = []
        for target in available_targets:
            if isinstance(target, CreatureCard):
                prio.append(target)
        return prio
