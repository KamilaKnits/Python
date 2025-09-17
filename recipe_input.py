# takes recipes from user, complies them and their ingredients
# into a list, stores all this in binary file for late use.
# script can be run again later to add more recipes

import pickle
import os

def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients)  >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients)  < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and len(ingredients) <= 4:
        difficulty = "Hard"
    
    return difficulty   

def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    ingredients_input = input("Enter ingredients separated by commas: ")
    ingredients = sorted(set(
        ingredient.strip().lower()
        for ingredient in ingredients_input.split(", ")))
    difficulty = calc_difficulty(cooking_time, ingredients)

    recipe = {
        "Name": name,
        "Cooking Time": cooking_time,
        "Ingredients": ingredients,
        "Difficulty": difficulty
    }

    return recipe, ingredients

 

filename = input("\n_______________________\n\nEnter the filename for your recipes: ")

data = {}
try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)

except FileNotFoundError:
    print("\n_______________________\n\nFile doesn't exist. Starting a new recipe list.")
    data = {
        "recipe_list": [],
        "all_ingredients":  []
    }
    
except:
    print("An unexpected error occurred.")
    data = {
        "recipe_list": [],
        "all_ingredients":  []
    }

else:
    file.close()

finally:
    recipes_list = data.get("recipe_list", [])
    all_ingredients = data.get("all_ingredients", [])

n = int(input("\n_______________________\n\nHow many recipes would you like to enter? \n_______________________\n\n"))

for i in range(n):
     recipe, ingredients = take_recipe()
     
     for ingredient in ingredients:
          if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

     recipes_list.append(recipe)

data = {
    "recipe_list": recipes_list,
    "all_ingredients": all_ingredients
}

with open(filename, 'wb') as file:
    pickle.dump(data, file)

print("Recipes saved successfully!")