# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: rschimme <rschimme@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 18:54:27 by rschimme        #+#    #+#               #
#  Updated: 2026/02/16 20:13:45 by rschimme        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def read_text() -> None:
    print("Initializing new storage unit: new_discovery.txt")
    try:
        file1 = open("new_discovery.txt", 'w')
        print("Storage unit created successfully\n")
    except FileNotFoundError:
        file1.close()
        print("error")
        return
    print("Inscribing preservation data...")
    file1.write("[ENTRY 001] New quantum algorithm discovered\n")
    file1.write("[ENTRY 002] Efficiency increased by 347%\n")
    file1.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    file1.close()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.\n")
    print("Now reading the file created")
    try:
        file1 = open("new_discovery.txt", 'r')
    except FileNotFoundError:
        file1.close()
        print("error")
        return
    data: str = file1.read()
    print(data)
    file1.close()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    read_text()
