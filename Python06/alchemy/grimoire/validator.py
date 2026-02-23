def validate_ingredients(ingredients: str) -> str:
    for ing in ingredients.split():
        if ing not in ["fire", "water", "air", "earth"]:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
