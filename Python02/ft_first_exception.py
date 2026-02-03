# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 17:19:09 by rschimme        #+#    #+#               #
#  Updated: 2026/02/03 17:46:46 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# def ft_first_exception():

def check_temperature(temp_str: str) -> None:

    try:
        int(temp_str)
        temperature = int(temp_str)
        print(f"{temperature} degrees")
    except:
        print("error")
    # temperature = int(temp_str)
    # print(f"{temperature} degrees")



if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    check_temperature("AB2")
