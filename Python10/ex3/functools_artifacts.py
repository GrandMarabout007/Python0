import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == 'add':
        return functools.reduce(operator.add, spells)
    if operation == 'multiply':
        return functools.reduce(operator.mul, spells)
    if operation == 'max':
        return max(spells)
    if operation == 'min':
        return min(spells)
    raise ValueError(f'operation {operation} not supported')


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = functools.partial(base_enchantment, 50, 'fire')
    ice = functools.partial(base_enchantment, 50, 'fire')
    lightning = functools.partial(base_enchantment, 50, 'lightining')

    return {
        'fire_enchant': fire,
        'ice_enchant': ice,
        'lightning_enchant': lightning,
    }


@functools.lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('use a number >= 0')
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


@functools.singledispatch
def spell_dispatcher() -> callable:
    raise ValueError("type not supported")


@spell_dispatcher.register(int)
def handle_damage(spell_damage: int):
    return f'{spell_damage} damages dealt'


@spell_dispatcher.register(str)
def handle_enchantment(enchantment: str):
    return f'{enchantment} casted'


@spell_dispatcher.register(list)
def handle_multi_cast(multi_cast: list):
    return [spell_dispatcher(item) for item in multi_cast]


def base_enchant(power: int, element: str, target: str):
    return f"Enchanting {target} with {power} power of {element}"


def main() -> None:

    print('\nTesting spell reducer..')
    spell_powers = [40, 45, 39, 12, 30, 35]
    print('Multiply:', spell_reducer(spell_powers, 'multiply'))
    print('Max:', spell_reducer(spell_powers, 'max'))
    print('Min:', spell_reducer(spell_powers, 'min'))
    print('Add:', spell_reducer(spell_powers, 'add'))

    print('\nTesting partial enchanter...')
    enchantments = partial_enchanter(base_enchant)
    cast_fire = enchantments['fire_enchant']
    print(cast_fire("Sword"))
    print(enchantments['ice_enchant']("Shield"))
    print(enchantments['lightning_enchant']("Staff"))

    print('\nTesting memoized fibonacci...')
    print(f'Fib(10): {memoized_fibonacci(10)}')
    print(f'Fib(15): {memoized_fibonacci(15)}')

    print('\nTesting spell_dispatcher...')
    print(spell_dispatcher(5))
    print(spell_dispatcher('fireball'))
    print(spell_dispatcher(['fireball', 'ice freeze', 'lightning bolt', 8]))


if __name__ == "__main__":
    main()
