# accesses binary file and lists all the ingredients that are available.
# User enters an ingredient, script displays recipe containing
# that specific ingredient

import pickle


def display_recipe(recipe):
    print("\n_______________________\n\nRecipe Found: \n_______________________\n\n")
    print(f"Name: {recipe['Name']}")
    print(f"Cooking Time: {recipe['Cooking Time']} minutes")
    print("Ingredients: ")
    for ingredient in sorted(recipe['Ingredients']):
        print(f"-{ingredient}")

    print(f"Difficulty: {recipe['Difficulty']}\n")
    


def search_ingredient(data):
    ingredients = sorted(ingredient.lower() for ingredient in data.get("all_ingredients", []))

    print("\n_______________________\n\nAvailable Ingredients: \n_______________________\n\n")
    
    for index, ingredient in enumerate (ingredients, start=1):
        print(f"{index}: {ingredient}")

    try:
        choice = int(input("\n_______________________\n\nEnter the number of the ingredient you would like to search for: "))
        ingredient_searched = ingredients[choice -1]
        print("\n_______________________\n\nSearching for recipes with:", ingredient_searched)
    
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number from the list.")
    
    else:
        found = False
        for recipe in data.get("recipe_list", []):
            if ingredient_searched in recipe["Ingredients"]:
                display_recipe(recipe)
                found = True
        if not found:
            print(f"\n_______________________\n\nNo recipes found containing '{ingredient_searched}'.")

filename = input("\n_______________________\n\nEnter the filename containing your recipes: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("Recipe file not found.")

else:
    search_ingredient(data)

