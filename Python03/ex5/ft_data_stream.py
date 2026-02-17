# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 16:05:57 by rschimme        #+#    #+#               #
#  Updated: 2026/02/17 14:23:21 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator


def fibonacci(number: int) -> Generator[int, None, None]:
    """Generator version of fibonnaci

    Args:
        number (int): number of iterations

    Yields:
        Generator[int, None, None]: the result of the fibonnaci
    """
    a: 'int' = 0
    b: 'int' = 1
    for i in range(number):
        add: 'int' = a + b
        yield (a)
        a = b
        b = add


def fibonnaci_stored(number: int) -> dict[int]:
    """Stored version of the fibonnaci

    Args:
        number (int): number of iterations

    Returns:
        dict[int]: dict containing all of the results for each iteration
    """
    a: 'int' = 0
    b: 'int' = 1
    result: 'dict' = []
    for i in range(number):
        add: 'int' = a + b
        result.append(a)
        a = b
        b = add
    return (result)


def create_events(number: int) -> Generator[dict, None, None]:
    """This fuction create fake random events with i as a base

    Args:
        number (int): number of events to create

    Yields:
        Generator[dict, None, None]: return a dict containing the data of
        the event
    """
    players: 'dict[str]' = ['alice', 'bob', 'charlie']
    actions: 'dict[str]' = ['killed monster', 'found treasure', 'leveled up',
                            "ate a carrot", "took a nap"]
    return_dict: 'dict' = ['0', '0', '0']
    for i in range(number):
        return_dict[0] = players[(((i % 7) + (i % 4) + i) % len(players))]
        return_dict[1] = ((i % 3) + (i % 11) + (i % 56) + (i % 89) + i) % 100
        return_dict[2] = actions[(((i % 3) + (i % 2) + i) % len(actions))]
        yield return_dict


def data_stream() -> None:

    i = 20
    print(f"Procesing {i} game events...")
    gen_dict: 'dict' = []
    high_level: 'int' = 0
    treasure: 'int' = 0
    levelup: 'int' = 0
    events: 'Generator[dict, None, None]' = create_events(i + 1)
    for n in range(i):
        gen_dict = next(events)
        if gen_dict[2] is ("ate a carrot" or "took a nap"):
            print(f"Event {n+1}: Bad stuff, filtered")
        else:
            print(f"Event {n+1}: Player {gen_dict[0]} (level {gen_dict[1]}) \
{gen_dict[2]}")
        if gen_dict[1] >= 60:
            high_level += 1
        if gen_dict[2] == "found treasure":
            treasure += 1
        if gen_dict[2] == "leveled up":
            levelup += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {i}")
    print(f"High level players (60+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}")
    demonstration()


def demonstration() -> None:
    print("\n=== Generator Demonstration ===")
    n = 10
    fib = fibonacci(n)
    print(f"Fibonacci sequence (first {n}) - stream everything:", end=' ')
    for number in range(n):
        if number == n-1:
            print(next(fib))
        else:
            print((next(fib)), end=', ')
    n = 5
    print(f"Fibonacci sequence (first {5}) - store everything: ", end='')
    print(fibonnaci_stored(n))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    data_stream()
