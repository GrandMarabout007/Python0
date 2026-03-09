from ex3.FantasyCardFactory import FantasyCardfactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():

    print('\n=== DataDeck Game Engine ===\n')

    print('Configuring Fantasy Card Game...')
    factory = FantasyCardfactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print(factory.get_supported_types())

    print("\nTurn execution:")
    print('Actions:', engine.simulate_turn())

    print()
    print('Game Report: ', engine.get_engine_status())


if __name__ == "__main__":
    main()
