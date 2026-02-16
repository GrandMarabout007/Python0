# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 18:35:15 by rschimme        #+#    #+#               #
#  Updated: 2026/02/16 19:38:37 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def read_text() -> None:
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        f1 = open("ancient_fragment.txt")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        f1.close()
        return
    print("Connection established...\n")
    data: str = f1.read()
    print("RECOVERED DATA:")
    print(data, "\n")
    print("Data recovery complete. Storage unit disconnected.")
    f1.close()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    read_text()
