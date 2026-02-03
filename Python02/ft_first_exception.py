# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 17:19:09 by rschimme        #+#    #+#               #
#  Updated: 2026/02/03 19:52:28 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# def ft_first_exception():
def test_temperature_input():

    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")

def check_temperature(temp_str: str) -> int:

    print(f"Testing temperature: {temp_str}")
    try:
        int(temp_str)
    except:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    temperature = int(temp_str)
    if (temperature >= 0) & (temperature <= 40):
        print(f"Temperature {temperature}°C is perfect for plants!\n")
        return temperature
    elif (temperature < 0):
        print(f"Error: {temperature}°C is too cold for plants (min 0°C)\n")
    else:
        print(f"Error: {temperature}°C is too hot for plants (max 40°C)\n")



if __name__ == "__main__":
    test_temperature_input()
