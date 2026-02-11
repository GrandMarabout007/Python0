# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/10 15:09:36 by rschimme        #+#    #+#               #
#  Updated: 2026/02/11 14:16:49 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_achievement_tracker():

    alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = set(['treasure_hunter', 'level_10', 'boss_slayer',
                  'speed_demon', 'perfectionist'])
    players = [("Alice", alice), ("Bob", bob), ("Charlie", charlie)]
    for name, achievement in players:
        print(f"Player {name} achievements: {[achievement]}")
    print("\n=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")
    common = alice.intersection(bob, charlie)
    print(f"Common to all players: {common}")
    rare_alice = alice.difference(bob.union(charlie))
    rare_bob = bob.difference(alice.union(charlie))
    rare_charlie = charlie.difference(alice.union(bob))
    rare_achievements = rare_alice.union(rare_bob).union(rare_charlie)
    print(f"Rare achievements (1 player): {rare_achievements}")
    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")
    print("\n=== Missing achievements ===")
    print(f"Alice missing achievements: {unique.difference(alice)}")
    print(f"Bob missing achievements: {unique.difference(bob)}")
    print(f"Charlie missing achievements: {unique.difference(charlie)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    ft_achievement_tracker()
