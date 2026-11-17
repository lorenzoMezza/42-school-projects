from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lowered = ingredients.lower()
    allowed = light_spell_allowed_ingredients()
    is_valid = any(ingredient in lowered for ingredient in allowed)
    if is_valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
