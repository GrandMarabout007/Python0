# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rschimme <rschimme@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 19:11:09 by rschimme          #+#    #+#              #
#    Updated: 2026/01/21 19:45:41 by rschimme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	days = input("Days since last watering: ")
	if int(days) > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")
