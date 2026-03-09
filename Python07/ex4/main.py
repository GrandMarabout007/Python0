from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main():

    print("\n === DataDeck Tournament Platform ===\n")
    platform = TournamentPlatform()

    print('\nRegistering Tournament Cards...\n')
    card1 = TournamentCard("Goblin", 3, 'common', 2, 1, 800)
    card2 = TournamentCard("Dragon", 11, 'legendary', 40, 21, 1300)
    platform.register_card(card1)
    platform.register_card(card2)
    platform.display_cards()

    print('Creating tournament match...')
    print('Match result:', platform.create_match(card1.id, card2.id))
    print('Match result:', platform.create_match(card2.id, card1.id))

    print('\nTournament Leaderboard:')
    platform.print_leaderboard()

    print('\nPlatform Report:')
    print(platform.generate_tournament_report())


if __name__ == "__main__":
    main()
