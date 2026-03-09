from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.registered: dict = {}
        self.matches: int = 0
        self.status: str = 'active'

    def register_card(self, card: TournamentCard) -> str:
        count: int = 1
        while True:
            new_id = f"{card.name}_{count:03d}"
            if new_id not in self.registered:
                break
            count += 1
        self.registered[new_id] = card
        card.id = new_id
        return new_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.registered or card2_id not in self.registered:
            raise ValueError
        if (self.registered[card1_id].damage >=
           self.registered[card2_id].damage):
            winner: str = card1_id
            loser: str = card2_id
        else:
            winner = card2_id
            loser = card1_id
        self.registered[winner].victories += 1
        self.registered[loser].defeats += 1
        self.registered[winner].calculate_rating()
        self.registered[loser].calculate_rating()
        self.matches += 1
        return {
            'winner': winner,
            'loser': loser,
            'winner_rating': self.registered[winner].rating,
            'loser_rating': self.registered[loser].rating,
        }

    def get_leaderboard(self) -> list:
        return sorted(self.registered.values(),
                      key=lambda card: card.rating, reverse=True)

    def print_leaderboard(self):
        leaderboard: list = self.get_leaderboard()
        i: int = 1
        for card in leaderboard:
            print(f'{i}. {card.name} - Rating: {card.rating} \
({card.victories}-{card.defeats})')
            i += 1

    def generate_tournament_report(self) -> dict:
        avg_rating: int = 0
        i: int = 0
        for card in self.registered.values():
            avg_rating += card.rating
            i += 1
        avg_rating = avg_rating/i

        return {
            'total_cards': len(self.registered.keys()),
            'matches_played': self.matches,
            'avg_rating': avg_rating,
            'platform_status': self.status
        }

    def display_cards(self):
        for card in self.registered.values():
            print(card.name, f'(ID: {card.id}):')
            print(f"- Interfaces: [\
{', '.join(base.__name__ for base in card.__class__.__bases__)}]")
            print(f'- Rating: {card.rating}')
            print(f'- Record: {card.victories}-{card.defeats}\n')
