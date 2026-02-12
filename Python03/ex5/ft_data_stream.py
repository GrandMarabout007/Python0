# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 16:05:57 by rschimme        #+#    #+#               #
#  Updated: 2026/02/12 17:25:49 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def fibonacci(number):
    result = []
    a = 0
    b = 1
    for i in range(number):
        add = a + b
        result.append(str(a))
        a = b
        b = add
    return result

# def create_events():
#     players = ['alice', 'bob', 'charlie']
#     actions = ['killed monster', 'found treasure', 'leveled up']
#     for x in range(10):


def data_stream():
    print(fibonacci(10))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    data_stream()
