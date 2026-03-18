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


# def partial_enchanter(base_enchantment: callable) -> dict[str, callable]
# def memoized_fibonacci(n: int) -> int
# def spell_dispatcher() -> callable

spell_powers = [40, 45, 39, 12, 30, 35]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [15, 19, 18]

def main() -> None:
    print(spell_reducer(spell_powers, 'multiply'))
    print(spell_reducer(spell_powers, 'max'))
    print(spell_reducer(spell_powers, 'min'))
    print(spell_reducer(spell_powers, 'add'))


if __name__ == "__main__":
    main()