import sqlalchemy
import sys
from sqlalchemy import create_engine, or_, Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://cf-python:password@localhost/task_database")
Session = sessionmaker(bind=engine)
session = Session()

Base = sqlalchemy.orm.declarative_base()

class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # helps identitfy objects easily from the terminal
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
    def __str__(self):
        ingredients_list = self.ingredients
        return (
            f"Recipe: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}"
        ) 
    
    def calculate_difficulty(self):
        ingredients_list = self.ingredients.split(", ")
        if self.cooking_time < 10 and len(ingredients_list) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(ingredients_list) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(ingredients_list) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"
    
    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        else:
            ingredient_list = [i.strip() for i in self.ingredients.split(", ")]
            return ingredient_list
    
    
# creates the tables of all models defined
Base.metadata.create_all(engine)

def get_input(prompt):
    user_input =  input(prompt).strip()
    if user_input.lower() == "exit":
        print("\n Exiting...")
        session.commit()
        session.close()
        exit()
    return user_input

def get_valid_name():
    # validate recipe by name
    while True: 
        name = get_input("\nEnter recipe name (max 50 characters, letters only) or type 'exit' to exit: ").strip()
        if len(name) > 50:
            print("❌ Name is too long...")
        elif not name.replace(" ", "").isalpha():
            print("❌ Name can only contain letters Try again...")
        else:
            return name

def get_valid_ingredient_count():
    while True:
        count = get_input("\nHow many ingredients would you like to enter? Type 'exit' to exit. ").strip()
        if count.isnumeric() and int(count)> 0:
            return int(count)
        print("❌ Please end a valid number greater than zero.")           
    
        
def get_ingredients(count):
     # collect ingredients one by one
    ingredients = []
    for i in range(count):
        while True:
            item = get_input(f"\nEnter ingredient #{i+1} (letter and spaces only), or type 'exit' to cancel: ").strip()
            if item.replace(" ", "").isalpha():
                ingredients.append(item)
                break
            print("❌ Ingredient must contain only letters and spaces.")
    return ", ".join(ingredients)
    
        
def get_valid_cooking_time():    
    # validate cooking time
    while True:
        cooking_time_input = get_input("\nEnter cooking time in minutes (or type 'exit' to exit): ")
        if cooking_time_input.isnumeric():
            return int(cooking_time_input)
        print("❌ Cooking time must be a number.")
    
def create_recipe():
    # create and save recipe
    name = get_valid_name()
    ingredient_count = get_valid_ingredient_count()
    ingredients = get_ingredients(ingredient_count)

    if len(ingredients) > 255:
        print("\n❌ Ingredients list is too long. Please shorten your entries.")
        return

    cooking_time = get_valid_cooking_time()  
     
    recipe_entry = Recipe(
        name = name,
        ingredients=ingredients,
        cooking_time=cooking_time,
        )

    recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()

    print("\n✅ Recipe added successfully!")
    print("-" * 40)
    print(recipe_entry)
    print("-" * 40)

    print("\nReturning to main menu...")

def view_all_recipes():   
    recipes = session.query(Recipe).all()
    if not recipes:
        print("\n❌ No recipes found...")
        return None
    
    print("\n📖All Recipes")
    print("=" * 40)

    for recipe in recipes:
        print(recipe)
        print("-" * 40)
    
    print("\nReturning to the main menu...")
    
      
def search_by_ingredients():

    # check if recipes exist
    recipe_count = session.query(Recipe).count()
    if recipe_count ==0:
        print("\n❌ No recipes found...")
        return None
    
    # retrieve all ingredients from table
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []

    # extract ingredients; make sure no duplicates
    for recipe in results:
        temp_list = [i.strip() for i in recipe.ingredients.split(",")]
        for item in temp_list:
            if item and item not in all_ingredients:
                all_ingredients.append(item)
    
    # display ingredients with numbers
    print("\nAvailable ingredients: ")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")
    
    # ask user to chose ingredients by number
    selected_input = get_input("\nEnter the number of the ingredient you would like to search for (or type 'exit' to exit): ").strip()
    selected_numbers = [num.strip() for num in selected_input.split(", ")]
    
    search_ingredients = []
    for num in selected_numbers:
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(all_ingredients):
                ingredient = all_ingredients[index]
                if ingredient not in search_ingredients:
                    search_ingredients.append(ingredient)
            else:
                print(f"\n❌ Invalid number: {num}")
        else:
            print(f"\n❌ Not a number {num}")

    if not search_ingredients:
        print("❌ No valid ingredients slected.")
        return
    
    # search for recipes containing selected ingredient
    print(f"\n🔍 Searching for recipes with: {', '.join(search_ingredients)}")
    matching_recipes = session.query(Recipe).filter(
        or_(*[Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients])).all()
    
    
    #print results
    if matching_recipes:
        print("\n✅ Matching recipes:")
        for recipe in matching_recipes:
            print("-" * 40)
            print(recipe)
            print("-" * 40)
        
        print("\nReturning to the main menu...")   
    
    else:
        print("\n❌ No recipes found with those ingredients.")


def edit_recipe():

    # check if recipes exist
    recipe_count = session.query(Recipe).count()
    if recipe_count ==0:
        print("\n❌ No recipes found...")
        return None
    
    # get id and name for each recipe from databse
    results = session.query(Recipe.id, Recipe.name).all()

    # display recipes to user
    print("\nAvailable recipes: ")
    for recipe_id, name in results:
        print(f"ID: {recipe_id} - {name}")
    
    # ask user to pick recipe by ID
    try:
        selected_id = int(get_input("\nEnter the ID of the recipe you want to update (or type 'exit' to exit): "))
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return
    
    # retrieve full recipe
    recipe_to_edit = session.get(Recipe, selected_id)
    if not recipe_to_edit:
        print("❌ No recipe found with that ID.")
        return
    
    # display editable fields
    print("\n🔧 Selected Recipe:")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking Time: {recipe_to_edit.cooking_time} minutes")
    print("Note: Difficulty is auto-calculated and cannot be edited directly.")

    
    # ask which field to edit
    choice = get_input("\nEnter the number of the attribute you'd like to edit (or type 'exit' to exit): ").strip()
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice")
        return
    
    # edit attribute
    if choice == "1":
        new_name = get_input("\nEnter new name(max 50 characters, letters and spaces only) or type 'exit' to exit: ")
        if len(new_name) > 50 or not new_name.replace(" ", "").isalpha():
            print("❌ Invalid name.")
            return
        recipe_to_edit.name = new_name
    
    elif choice == "2":
        new_ingredients = get_input("Enter new ingredients (max 255 characters, separated by comma) or 'exit' to exit: ").strip()
        if len(new_ingredients) > 255 or not all(i.strip().replace(" ", "").isalpha
                                                 for i in new_ingredients.split(",")):
            print("❌ Invalid ingredients format.")
            return
        recipe_to_edit.ingredients = new_ingredients

    elif choice == "3":
        new_time = get_input("Enter new cooking time in minutes ( or type 'exit' to exit): ").strip()
        if not new_time.isnumeric():
            print("❌ Cooking time must be a number.")
        recipe_to_edit.cooking_time = int(new_time)


    # recalculate difficulty and commit
    recipe_to_edit.calculate_difficulty()    
    session.commit()
    print("\n✅ You did it! here is the updated version:\n")
    print(f"Recipe: {recipe_to_edit}")
    print("\nReturning to the main menu...")
   
def delete_recipe():
    # check if recipes exist
    recipe_count = session.query(Recipe).count()
    if recipe_count ==0:
        print("\n❌ No recipes found...")
        return None
    
    # get id and name for each recipe from databse
    results = session.query(Recipe.id, Recipe.name).all()

    # display recipes to user
    print("\n📋 Available recipes: ")
    for recipe_id, name in results:
        print(f"\nID: {recipe_id} - {name}")
    
    # ask user recipe to delete by ID
    try: 
        selected_id = int(input("\nEnter the number of the recipe you'd like to delete (or type 'exit' to exit): ").strip())
    
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    # retrieve recipe by ID

    recipe_to_delete = session.get(Recipe, selected_id)
    if not recipe_to_delete:
        print("❌ No recipe found with that ID.")
        return

    # ask user if they're sure they want to delete recipe. if yes, delete recipe and commit
    confirm = input(f"\nAre you sure you want to delete '{recipe_to_delete.name}'(yes/no)? ")
    if confirm != "yes":
        print("\nCancelling...")
        return
   
    
    session.delete(recipe_to_delete)
    session.commit()
    print(f"\n✅ You did it! '{recipe_to_delete.name}' has been deleted.")
    print("\nReturning to the main menu...")
    
def main_menu():
    while True:
        print("\n")
        print("\nMain Menu")
        print("\n============================")
        print("\nWhat would you like to do?\n")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for a recipe by ingredients")
        print("4. Edit an existing recipe")
        print("5. Delete a recipe")
        print("6. Exit the program")
        print("\n")

        choice = get_input("Your choice: ")

        if choice =='1':
            create_recipe()
    
        elif choice == '2':
            view_all_recipes()

        elif choice == '3':
            search_by_ingredients()

        elif choice == '4':
             edit_recipe()

        elif choice == '5':
             delete_recipe()   
    
        elif choice == '6':
            print("\n")
            print("Exiting the program...\n")
            session.commit()
            session.close()
            break
        else:
            print("Invalid choice, please try again.")

main_menu()