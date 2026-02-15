# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/14 17:16:48 by rschimme        #+#    #+#               #
#  Updated: 2026/02/14 17:18:48 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def list_example():
    print("=== List comprehension Examples ===")
    players = [
        ('alice', 1800, True),
        ('charlie', 2500, True),
        ('bob', 3650, False),
        ('diana', 600, False),
        ]
    high_scores = [name for name, score, a in players if score > 2000]
    print(f"High scorers (>2000): {high_scores}")
    double_scores = [(score * 2) for n, score, a in players]
    print(f"Scores doubled: {double_scores}")
    active_p = [name for name, s, active in players if active is True]
    print(f"Active players: {active_p}")


def dict_example():
    print("=== Dict comprehension Examples ===")
    players = [
        ('alice', 1800),
        ('charlie', 2500),
        ('bob', 3650),
        ('diana', 600),
        ]
    players_dict = {name: score for name, score in players}
    print(f"Player scores: {players_dict}")
    # categories = {"high": 0, "medium": 0, "low": 0}
    # for score in players_dict.values():
    #     if score >= 2000:
    #         categories["high"] += 1
    #     elif score >= 1000:
    #         categories['medium'] += 1
    #     else:
    #         categories['low'] += 1
    categories = {
        "high": sum(1 for score in players_dict.values() if score > 2000),
        "medium": sum(1 for score in players_dict.values() if 1000 <= score <= 2000),
        "low": sum(1 for score in players_dict.values() if score < 1000)
    }
    print(categories)


def set_example():


if __name__ == "__main__":
    print("=== Game Acalytics Dashboard ===\n")
    list_example()
    print()
    dict_example()