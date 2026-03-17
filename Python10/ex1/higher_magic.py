


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args, **kwargs: (spell1(*args, **kwargs), spell2(*args, **kwargs))

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier
def conditional_caster(condition: callable, spell: callable) -> callable:
    pass
def spell_sequence(spells: list[callable]) -> callable:
    pass



def fireball(power: int) -> str:
    return 80

def mana_cost(power: int) -> int:
    return power // 2

test_values = [7, 6, 19]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

def main() -> None:
    fire_and_drain = spell_combiner(fireball, mana_cost)
    print(fire_and_drain(100))
    amplified = power_amplifier(fire_and_drain, 2)
    print(amplified(100))
    print(power_amplifier(fireball, 2)(80))


if __name__ == "__main__":
    main()