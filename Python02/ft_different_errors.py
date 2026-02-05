# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 14:16:22 by rschimme        #+#    #+#               #
#  Updated: 2026/02/05 20:09:15 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def test_error_types() -> None:

    file_to_send = "missing.txt"
    something = "plant"
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("value", file_to_send, something)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero", file_to_send, something)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file", file_to_send, something)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file_to_send}'\n")
    print("Testing KeyError...")
    try:
        garden_operations("key", file_to_send, something)
    except KeyError:
        print(f"Caught KeyError: 'missing {something}'\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("value", file_to_send, something)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


def garden_operations(keyword: str, arg: str, smth: str) -> None:

    smth = {}
    if keyword == "value":
        int("abc")
    elif keyword == "zero":
        42 / 0
    elif keyword == "file":
        open(arg)
    elif keyword == "key":
        print({smth["pat"]})


if __name__ == "__main__":
    test_error_types()
