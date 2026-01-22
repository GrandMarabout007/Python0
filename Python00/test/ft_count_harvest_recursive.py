# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rschimme <rschimme@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 19:38:26 by rschimme          #+#    #+#              #
#    Updated: 2026/01/21 20:00:45 by rschimme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def count_recursive(val, days):
	if val > 0:
		print(f"Day {days}")
		return (count_recursive(val-1, days+1))
	return(1)

def ft_count_harvest_recursive():
	days = input("Days until harvest: ")
	val = int(days)
	days = 1
	count_recursive(val, days)
	print("Harvest time!")

if __name__ == "__main__":
	ft_count_harvest_recursive()