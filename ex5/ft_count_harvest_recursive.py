# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rschimme <rschimme@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 19:38:26 by rschimme          #+#    #+#              #
#    Updated: 2026/01/22 14:27:03 by rschimme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    val = days
    days = 1

    def _count_recursive(val, days):
        if val > 0:
            print(f"Day {days}")
            _count_recursive(val-1, days+1)
    _count_recursive(val, days)
    print("Harvest time!")

if __name__ == "__main__":
    ft_count_harvest_recursive()