# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rschimme <rschimme@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 18:39:09 by rschimme          #+#    #+#              #
#    Updated: 2026/01/21 19:45:29 by rschimme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
	length = input("Enter length: ")
	width = input("Enter width: ")
	plot = int(length) * int(width)
	print(f"Plot area: {plot}")
