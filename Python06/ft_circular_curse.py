from alchemy.grimoire import validate_ingredients, record_spell


def circular_curse_breaking() -> None:
    print("Testing ingredient validation:")
    ingredients1: str = "fire air"
    print(f"validate_ingredients(\"fire air\"): \
{validate_ingredients(ingredients1)}")
    ingredients2: str = "dragon scales"
    print(f"validate_ingredients(\"dragon scales\"): \
{validate_ingredients(ingredients2)}")
    print("\n Testing spell recording with validation:")
    record1: str = record_spell("Fireball", "fire air")
    print(f"record_spell(\"Fireball\", \"fire air\"): {record1}")
    record2: str = record_spell("Dark Magic", "shadow")
    print(f"record_spell((\"Dark Magic\", \"shadow\"): {record2}")
    print("\nTesting late import technique:")
    result3: str = record_spell("Lightning", "air")
    print(f"record_spell(\"Lightning\", \"air\"): {result3}")
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")
    circular_curse_breaking()
