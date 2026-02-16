# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 19:42:29 by rschimme        #+#    #+#               #
#  Updated: 2026/02/16 20:13:08 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def crisis_response(file1) -> None:
    try:
        with open(file1, 'r') as file001:
            data1: str = file001.read()
            print(f"SUCCESS: Archive recovered - ''{data1}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def test_crisis_system() -> None:
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    crisis_response('lost_archive.txt')
    print()
    print("CRISIS ALERT: Attempting access to 'classified_data.txt'...")
    crisis_response("classified_data.txt")
    print()
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    crisis_response("standard_archive.txt")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    test_crisis_system()
