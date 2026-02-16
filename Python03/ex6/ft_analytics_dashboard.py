# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/14 17:16:48 by rschimme        #+#    #+#               #
#  Updated: 2026/02/16 17:36:59 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def comprehension_examples():
    print("=== List comprehension Examples ===")
    players1 = [
        ('alice', 1800, True),
        ('charlie', 2500, True),
        ('bob', 3650, False),
        ('diana', 600, False),
        ]
    high_scores = [name for name, score, a in players1 if score > 2000]
    print(f"High scorers (>2000): {high_scores}")
    double_scores = [(score * 2) for n, score, a in players1]
    print(f"Scores doubled: {double_scores}")
    active_p = [name for name, s, active in players1 if active is True]
    print(f"Active players: {active_p}")
    print("\n=== Dict comprehension Examples ===")
    players2 = [
        ('alice', 1800),
        ('charlie', 2500),
        ('bob', 3650),
        ('diana', 600),
        ]
    players_dict = {name: score for name, score in players2}
    print(f"Player scores: {players_dict}")
    categories = {
        "high": sum(1 for score in players_dict.values() if score > 2000),
        "medium": sum(1 for score in players_dict.values()
                      if 1000 <= score <= 2000),
        "low": sum(1 for score in players_dict.values() if score < 1000)
    }
    print(f"Score categories: {categories}")
    alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = set(['treasure_hunter', 'level_10', 'boss_slayer',
                   'speed_demon', 'perfectionist'])
    achievements = [('alice', alice), ('bob', bob), ('charlie', charlie)]
    achievements_count = {
        name: len(achiev) for name, achiev in achievements
    }
    print(f"Acheviement counts: {achievements_count}")
    print("\n=== Set comprehension Examples ===")
    players3 = [
        ('alice', 1800),
        ('charlie', 2500),
        ('bob', 3650),
        ('alice', 500),
        ('alice', 1800),
        ('diana', 600),
        ('charlie', 20),
        ]
    players_unique = {name for name, score in players3}
    print(f"Unique players: {players_unique}")
    unique_achievements = {achiev for player_achiev in (alice, bob, charlie)
                           for achiev in player_achiev}
    print(f"Unique achievements: {unique_achievements}")
    print("\n=== Combined Analysis ===")
    total_players = len(players_unique)
    total_unique_achievements = len(unique_achievements)
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    average = sum(players_dict[name] for name in
                  players_dict) / len(players_dict)
    print(f"Average Score : {average}")
    top_performer_score = max(players_dict[name] for name in players_dict)
    top_performer_name = [name for name in players_dict if players_dict[name]
                          == top_performer_score][0]
    top_performer_achievement = achievements_count[top_performer_name]
    print(f"Top performer: {top_performer_name} ({top_performer_score} \
points, {top_performer_achievement} achievements)")


if __name__ == "__main__":
    print("=== Game Acalytics Dashboard ===\n")
    comprehension_examples()
