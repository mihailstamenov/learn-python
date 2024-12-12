def check_ingredient_match(recipe, ingredients):
    missing_ingredients =[]
    percentage = float(0)
    for i in range(0, len(recipe)):
        if recipe[i] != ingredients[i]:
            missing_ingredients.append(recipe[i])
    if len(missing_ingredients) == 0:
        percentage =  float(100)
    else:
        percentage = float(100-(len(missing_ingredients)/len(recipe)*100))
    return percentage, missing_ingredients

# percentage, missing_ingredients = check_ingredient_match(recipe, ingredients)
# Prints: 75.00 ["Unicorn Hair"]


# print()