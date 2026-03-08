from ex4.TournamentCard import TournamentCard



class TournamentPlatform:
    def __init__(self):
        self.registered: dict = {}

    def register_card(self, card: TournamentCard) -> str:
        count = 1
        while True:
            new_id = f"{card.name}_{count:03d}"
            if new_id not in self.registered:
                break
            count += 1
        self.registered[new_id] = card
        card.id = new_id
        card.rating = 1200
        return new_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id or card2_id not in self.registered:
            raise ValueError
        if self.registered[card1_id].attack >= self.registered[card2_id].attack:
            winner = card1_id
            loser = card2_id
        else:
            winner = card2_id
            loser = card1_id
        self.registered[winner].rating += 12
        self.registered[loser].rating -= 12
        return{
            'winner': winner,
            'loser': loser,
            'winner_rating': self.registered[winner].rating,
            'loser_rating': self.registered[loser].rating,
        }

    def get_leaderboard(self) -> list:
        return sorted(self.registered.values(), key=lambda card: card.rating, reverse=True)

    def generate_tournament_report(self) -> dict:
