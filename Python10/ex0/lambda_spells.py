
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    valid_mages = []
    for mage in mages:
        

# def spell_transformer(spells: list[str]) -> list[str]:

# def mage_stats(mages: list[dict]) -> dict:
    
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda x: x["power"], reverse=True))







def main():
    artifacts = [{'name': 'Crystal Orb', 'power': 114, 'type': 'weapon'},
                {'name': 'Light Prism', 'power': 102, 'type': 'relic'},
                {'name': 'Shadow Blade', 'power': 111, 'type': 'accessory'},
                {'name': 'Wind Cloak', 'power': 101, 'type': 'weapon'}]
    
    print(artifact_sorter(artifacts))

    mages = [{'name': 'Zara', 'power': 91, 'element': 'fire'},
            {'name': 'Riley', 'power': 56, 'element': 'lightning'},
            {'name': 'Nova', 'power': 82, 'element': 'wind'},
            {'name': 'Kai', 'power': 67, 'element': 'wind'},
            {'name': 'Sage', 'power': 68, 'element': 'light'}]

    spells = ['shield', 'flash', 'fireball', 'tornado']

if __name__ == "__main__":
    main()