# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rschimme <rschimme@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 19:01:05 by rschimme          #+#    #+#              #
#    Updated: 2026/01/21 19:45:32 by rschimme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day_1 = input("Day 1 harvest: ")
	day_2 = input("Day 2 harvest: ")
	day_3 = input("Day 2 harvest: ")
	total = int(day_1) + int(day_2) + int(day_3)
	print(f"Total harvest: {total}")
