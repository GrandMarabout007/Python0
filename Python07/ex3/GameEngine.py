from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class GameEngine:
    def __init__(self):
        self.turns: int = 0
        self.total_damage: int = 0
        self.total_created: int = 0
        self.__factory: CardFactory = None
        self.__strategy: GameStrategy = None
        self.__hand: list = []
        self.__battlefield: list = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.__factory: CardFactory = factory
        print(f"Factory: {self.__factory.__class__.__name__}")
        self.__strategy: GameStrategy = strategy
        print(f"Strategy: {self.__strategy.__class__.__name__}")

    def generate_hand(self, size: int) -> None:
        if not self.__hand:
            new_deck: list = self.__factory.create_themed_deck(size)
            for card in new_deck.values():
                self.total_created += 1
                self.__hand.append(card)

    def simulate_turn(self) -> dict:
        if self.__factory is None or self.__strategy is None:
            raise RuntimeError("Error: Run configure_engine() first")
        print(f"Strategy: {self.__strategy.__class__.__name__}")
        self.turns += 1
        if not self.__hand:
            self.generate_hand(4)
        turn_result: dict = (self.__strategy.execute_turn(self.__hand,
                             self.__battlefield))
        for card in self.__hand:
            if isinstance(card, CreatureCard):
                self.total_damage += card.attack

        return turn_result

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns,
            'strategy_used': self.__strategy.__class__.__name__,
            'total_damage': self.total_damage,
            'cards_created': self.total_created
        }
