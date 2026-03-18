def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args, **kwargs: (spell1(*args, **kwargs),
                                    spell2(*args, **kwargs))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *args, **kwargs: spell(*args, **kwargs) \
        if condition(*args, **kwargs) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args, **kwargs: [spell(*args, **kwargs) for spell in spells]


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def classic_attack() -> int:
    return 10


def has_mana(mana: int) -> bool:
    return mana >= 50


def magic_fireball(mana: int) -> str:
    return "magic fireball casted"


def main() -> None:
    print("\nTesting spell combiner...")
    healing_fireball = spell_combiner(fireball, heal)
    res1, res2 = healing_fireball("Dragon")
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(classic_attack, 2)
    print(f"Original: {classic_attack()}, Amplified: {amplified()}")

    print("\nTesting conditional caster...")
    magic_cast = conditional_caster(has_mana, magic_fireball)
    print('Cast with 20 mana :', magic_cast(20))
    print('Cast with 100 mana :', magic_cast(100))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, magic_fireball])
    print(f"Sequence result on Goblin: {sequence('Goblin')}")


if __name__ == "__main__":
    main()
