from functools import wraps
import time


def spell_timer(func: callable) -> callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Casting {func.__name__}...')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Spell completed in {(end-start):.6f} seconds')
        return result
    return wrapper


def power_validator(min_power: int) -> callable:

    def power_decorator(func: callable) -> callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return power_decorator


def retry_spell(max_attempts: int) -> callable:

    def retry_decorator(func: callable) -> callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            tries = 1
            while tries <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... \
(attempt {tries}/{max_attempts})")
                    tries += 1
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return retry_decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (len(name) >= 3) and name.replace(" ", "").isalpha():
            return True
        return False

    @staticmethod
    @power_validator(min_power=10)
    def cast_spell(power: int, spell_name: str) -> str:
        return f'Successfully cast {spell_name} with {power} power'


@spell_timer
def fire_spell(power: int):
    time.sleep(0.02)
    return f'fire spell casted with {power} power'


@power_validator(min_power=5)
def ice_spell(power: int):
    return f'ice spell casted with {power} power'


@retry_spell(max_attempts=6)
def cast_unstable_fireball(damage: str, _state: list = [0]) -> str:
    _state[0] += 1

    if _state[0] < 3:
        raise ValueError("the fireball was too unstable")

    return f"Fireball hits with {damage} damage!"


def main() -> None:
    print(fire_spell(10))

    print('\nTesting power validator...')
    print(ice_spell(10))
    print(ice_spell(4))

    print('\nTesting retry spell...')
    print(cast_unstable_fireball(10))

    print('\nTesting MageGuild...')
    print(MageGuild.validate_mage_name('Auguste the mage'))
    print(MageGuild.validate_mage_name('Fire_mage'))
    print(MageGuild.cast_spell(80, 'fire'))
    print(MageGuild.cast_spell(2, 'mud'))


if __name__ == "__main__":
    main()
