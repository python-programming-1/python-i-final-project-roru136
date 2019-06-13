import json
from pprint import pprint
#current_ingredients = ['tomato', 'cheese', 'lettuce', 'pickles', 'bread']
recipe_file = "full_format_recipes.json"


# def build_recipe_dictionary(recipe_file):
#     recipes = {}
#     with open(recipe_file, 'r') as f:
#         for line in f:
#             words = line.split()
#             if words:
#                 recipes[words[0]] = words[1:]
#     return recipes

def build_recipe_dictionary(recipe):
    recipes = {}
    with open(recipe) as f:
        d = json.load(f)

    for line in d:
        if 'title' in line:
            recipe = line['title']
            for ingredients in recipe:
                if 'ingredients' in ingredients:
                    ingredient = ingredients['ingredients']
                    print(ingredient)
    
            #recipes.append(line['title'])
            #recipes.append(line['ingredients'])
            #print(recipes)
            #print (d['title']['ingredients'])
            # print('Recipe: ' + line['title'])
            # print('Ingredients: ' + line['ingredients'])
            # print('')

            #words = line.split()
            #if words:
                #recipes['title'] = ['ingredients']

            pprint(line['title'])
            pprint(line['ingredients'])
            # store title as key and ingredients as value in dictionary
    return recipe
 

def check_for_recipes(current_ingredients, recipes):
    #for recipe, ingredients in recipes.items():
    for recipe, ingredient in enumerate(recipes):
        has_all_ingredients = True
        print(recipes.items())
        for ingredient in current_ingredients:
            if ingredient not in current_ingredients:
                #print("You do not have enough ingredients.")
                has_all_ingredients = False
                break
        if has_all_ingredients:
            print('You have the ingredients to make: {}'.format(title))
        elif not has_all_ingredients:
            print("You do not have enough ingredients.")
def get_user_input():
    print("Enter ingredients")
    ingredients = input()
    ingredient_list = ingredients.split()
    return ingredient_list


recipe_dict = build_recipe_dictionary(recipe_file)
#user_ingredients = get_user_input()
current_ingredients = get_user_input()
check_for_recipes(current_ingredients, recipe_dict)