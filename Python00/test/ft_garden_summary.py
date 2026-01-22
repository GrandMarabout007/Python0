# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rschimme <rschimme@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 14:48:25 by rschimme          #+#    #+#              #
#    Updated: 2026/01/22 14:54:06 by rschimme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
	name = input("Enter garden name: ")
	plants = int(input("Enter number of plants: "))
	print(f"Garden: {name}")
	print(f"Plants: {plants} ")
	print("Status: Growing well!")