
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map((lambda spell: '* '+spell+' *'), spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage['power'])
    min_power = min(mages, key=lambda mage: mage['power'])
    total_power = sum(map(lambda mage: mage['power'], mages))
    avg_power = total_power/len(mages)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg-power': avg_power,
    }


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda x: x["power"], reverse=True))


def main():
    artifacts = [{'name': 'Crystal Orb', 'power': 114, 'type': 'weapon'},
                 {'name': 'Light Prism', 'power': 102, 'type': 'relic'},
                 {'name': 'Shadow Blade', 'power': 111, 'type': 'accessory'},
                 {'name': 'Wind Cloak', 'power': 101, 'type': 'weapon'}]

    mages = [{'name': 'Zara', 'power': 91, 'element': 'fire'},
             {'name': 'Riley', 'power': 56, 'element': 'lightning'},
             {'name': 'Nova', 'power': 82, 'element': 'wind'},
             {'name': 'Kai', 'power': 67, 'element': 'wind'},
             {'name': 'Sage', 'power': 68, 'element': 'light'}]

    spells = ['shield', 'flash', 'fireball', 'tornado']
    print('\nTesting artifact sorter...')
    sorted_artifacts = (artifact_sorter(artifacts))
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} \
power) comes before {sorted_artifacts[1]['name']} \
({sorted_artifacts[1]['power']} power)")

    print('\nTesting power filter...')
    print(power_filter(mages, 68))

    print('\nTesting spell transformer...')
    spells_transformed = (spell_transformer(spells))
    for spell in spells_transformed:
        print(spell, ' ', end='')

    print('\n\nGetting mage stats...')
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
