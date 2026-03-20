def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def add_power(acc_power: int) -> None:
        nonlocal power
        power += acc_power
        return power

    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    enchantment = enchantment_type

    def enchant_item(item_name: str):
        item = enchantment + ' ' + item_name
        return item

    return enchant_item


def memory_vault() -> dict:
    memory = {}

    def store(key: str, value: any) -> None:
        memory[key] = value

    def recall(key: str) -> any:
        return memory.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main() -> None:

    print('\nTesting mage counter...')

    count = mage_counter()
    print('Call 1:', count())
    print('Call 2:', count())
    print('Call 3:', count())

    print('\nTesting spell accumulator with base 100...')
    acc = spell_accumulator(100)
    print(f"Adding 10: {acc(10)}")
    print(f"Adding 74: {acc(74)}")

    print('\nTesting enchantment factory...')
    print('Enchanting items with flame')
    fac = enchantment_factory('Flaming')
    print(f"Echanted : {fac('sword')}")
    print(f"Echanted : {fac('staff')}")

    print("\nTesting memory_vault...")
    vault = memory_vault()
    vault['store']("fire_spell", "Mega Fireball")
    vault['store']("ice_spell", 500)

    print(f"Recall 'fire_spell': {vault['recall']('fire_spell')}")
    print(f"Recall 'ice_spell': {vault['recall']('ice_spell')}")
    print(f"Recall 'healing': {vault['recall']('healing')}")


if __name__ == "__main__":
    main()
