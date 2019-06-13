
def get_user_input():
    print("Enter ingredients")
    ingredients = input()
    ingredient_list = ingredients.split()
    return ingredient_list


if __name__ == '__main__':
    recipes = {}
    current_ingredients = get_user_input()
    recipe_file = "recipes.txt"
    
    with open(recipe_file, 'r') as f:
        for line in f:
            words = line.split()
            if words:
                recipes[words[0]] = words[1:]

    make_anything = False
    for recipe, ingredients in recipes.items():
        for ingredient in ingredients:
            if ingredient not in current_ingredients:
                break
        else:
            print('You have the ingredients to make: {}'.format(recipe))
            make_anything = True
    if not make_anything:
        print('You do not have enough ingredients.')