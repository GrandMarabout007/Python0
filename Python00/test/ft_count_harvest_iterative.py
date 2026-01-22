# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rschimme <rschimme@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 19:26:48 by rschimme          #+#    #+#              #
#    Updated: 2026/01/21 19:34:35 by rschimme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	days = input("Days until harvest: ")
	val = int(days)
	days = 1
	while val > 0:
		print(f"Day {days}")
		days = int(days) + 1
		val = val - 1
	print("Harvest time!")
	
if __name__ == "__main__":
    ft_count_harvest_iterative()