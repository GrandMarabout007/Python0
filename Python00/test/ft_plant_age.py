# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rschimme <rschimme@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 19:06:48 by rschimme          #+#    #+#              #
#    Updated: 2026/01/21 19:45:36 by rschimme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	age = input("Enter plant age in days: ")
	if int(age) > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
