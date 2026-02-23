def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    result = validate_ingredients(ingredients)
    if "VALID" in result.split("-")[1]:
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
