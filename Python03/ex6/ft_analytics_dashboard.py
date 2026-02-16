# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/14 17:16:48 by rschimme        #+#    #+#               #
#  Updated: 2026/02/16 18:11:20 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def comprehension_examples() -> None:
    print("=== List comprehension Examples ===")
    players1: list[tuple[str, int, bool]] = [
        ('alice', 1800, True),
        ('charlie', 2500, True),
        ('bob', 3650, False),
        ('diana', 600, False),
        ]
    high_scores: list[str] = [name for name, score, a in players1
                              if score > 2000]
    print(f"High scorers (>2000): {high_scores}")
    double_scores: list[int] = [(score * 2) for n, score, a in players1]
    print(f"Scores doubled: {double_scores}")
    active_p: list[str] = [name for name, s, active in players1 if active
                           is True]
    print(f"Active players: {active_p}")
    print("\n=== Dict comprehension Examples ===")
    players2: list[tuple[str, int]] = [
        ('alice', 1800),
        ('charlie', 2500),
        ('bob', 3650),
        ('diana', 600),
        ]
    players_dict: dict[str, int] = {name: score for name, score in players2}
    print(f"Player scores: {players_dict}")
    categories: dict[str, int] = {
        "high": sum(1 for score in players_dict.values() if score > 2000),
        "medium": sum(1 for score in players_dict.values()
                      if 1000 <= score <= 2000),
        "low": sum(1 for score in players_dict.values() if score < 1000)
    }
    print(f"Score categories: {categories}")
    alice: set[str] = set(['first_kill', 'level_10', 'treasure_hunter',
                           'speed_demon'])
    bob: set[str] = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie: set[str] = set(['treasure_hunter', 'level_10', 'boss_slayer',
                            'speed_demon', 'perfectionist'])
    achievements: list[tuple[str, set[str]]] = [
        ('alice', alice),
        ('bob', bob),
        ('charlie', charlie)
    ]
    achievements_count: dict[str, int] = {
        name: len(achiev) for name, achiev in achievements
    }
    print(f"Acheviement counts: {achievements_count}")
    print("\n=== Set comprehension Examples ===")
    players3: list[tuple[str, int]] = [
        ('alice', 1800),
        ('charlie', 2500),
        ('bob', 3650),
        ('alice', 500),
        ('alice', 1800),
        ('diana', 600),
        ('charlie', 20),
        ]
    players_unique: set[str] = {name for name, score in players3}
    print(f"Unique players: {players_unique}")
    unique_achievements: set[str] = {achiev for player_achiev in
                                     (alice, bob, charlie)
                                     for achiev in player_achiev}
    print(f"Unique achievements: {unique_achievements}")
    print("\n=== Combined Analysis ===")
    total_players: int = len(players_unique)
    total_unique_achievements: int = len(unique_achievements)
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    average: float = sum(players_dict[name] for name in
                         players_dict) / len(players_dict)
    print(f"Average Score : {average}")
    top_performer_score: int = max(players_dict[name] for name in players_dict)
    top_performer_name: str = [name for name in players_dict if
                               players_dict[name] == top_performer_score][0]
    top_performer_achievement: int = achievements_count[top_performer_name]
    print(f"Top performer: {top_performer_name} ({top_performer_score} \
points, {top_performer_achievement} achievements)")


if __name__ == "__main__":
    print("=== Game Acalytics Dashboard ===\n")
    comprehension_examples()
