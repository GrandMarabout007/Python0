# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/09 17:16:45 by rschimme        #+#    #+#               #
#  Updated: 2026/02/09 18:15:20 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def score_analytics() -> None:
    import sys
    scores: list = []
    if len(sys.argv) == 1:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} \
<score1> <score2> ...")
        return
    try:
        for arg in sys.argv[1:]:
            scores.append(int(arg))
    except ValueError:
        print("Error: use only numbers as scores")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(sys.argv) - 1}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score = {(sum(scores) / (len(sys.argv) - 1))}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {(max(scores) - min(scores))}\n")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
