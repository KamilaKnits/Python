import mysql.connector

conn = mysql.connector.connect(
   host='localhost',
   user='cf-python',
   passwd='password')

# print("connetion worked")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

cursor.execute("""CREATE TABLE IF NOT EXISTS recipes(
               item_id INT AUTO_INCREMENT PRIMARY KEY, 
               name VARCHAR(50), 
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20)
               )
               """)

conn.commit()

def calculate_difficulty(cooking_time, ingredients_list):
    if cooking_time < 10 and len(ingredients_list) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients_list) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients_list) < 4:
        return "Intermediate"
    elif cooking_time >= 10 and len(ingredients_list) <= 4:
        return "Hard"
               

def create_recipe(conn,cursor):
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (separated by comma): ")
    cooking_time = int(input("Enter cooking time in minutes: "))

    ingredients_list = ingredients.split(", ")
    difficulty = calculate_difficulty(cooking_time, ingredients_list)

    query = """
        INSERT INTO recipes (name, ingredients, cooking_time, difficulty)
        VALUES (%s, %s, %s, %s)
        """       
    values = (name, ingredients, cooking_time, difficulty)

    cursor.execute(query, values)
    conn.commit()
    print("Your did it! Recipe added successfully.")


def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM recipes") 
    results = cursor.fetchall()

    all_ingredients = set(
        i.strip().lower()
        for row in results
        for i in row[0].split(", ")      
    )
    
    print("\nAvailable ingredients: ")
    print("\n")
    for i, ingredient in enumerate(sorted(all_ingredients), start=1):
        print(f"{i}. {ingredient}")

    try:
        choice = int(input("\nEnter the number of the ingredient you'd like to search for: "))
        ingredient_list = sorted(all_ingredients)
        search_term = ingredient_list[choice -1]
    except(ValueError, IndexError):
        print("Invalid selection. Please enter a valid number from the list.")
        return

    query = "SELECT * FROM recipes WHERE LOWER(ingredients) LIKE %s"
    cursor.execute(query,('%' + search_term + '%',))
    search_ingredient = cursor.fetchall()
    
    if search_ingredient:
        print("\nRecipes that contain this ingredient:")
        for recipe in search_ingredient: 
            item_id, name, ingredients, cooking_time, difficulty = recipe
            print(f"\nID: {item_id}")
            print(f"Name: {name}")
            print(f"Ingredients: {ingredients}")
            print(f"Cooking Time: {cooking_time} minutes")
            print(f"Difficulty: {difficulty}")
    else:
        print("Sorry, no recipes found with that ingredient.")

    conn.commit()

def update_recipe(conn, cursor):
    
    cursor.execute("SELECT item_id, name, ingredients, cooking_time, difficulty FROM recipes") 
    recipes = cursor.fetchall()

    if not recipes:
        print("Sorry, no recipe found with that name")
        return
    
    print("\nAvailable recipes: ")
    for recipe in recipes:
        item_id, name, ingredients, cooking_time, difficulty = recipe
        print(f"\nID: {item_id}")
        print(f"Name: {name}")
        print(f"Ingredients: {ingredients}")
        print(f"Cooking Time: {cooking_time} minutes")
        print(f"Difficulty: {difficulty}")
    try:
        recipe_id = int(input("\nEnter the ID of the recipe you want to update: "))
    except ValueError:
        print("Invalid ID. please enter a number.")
        return
    
    cursor.execute("SELECT * FROM recipes WHERE item_id = %s",(recipe_id,))
    selected = cursor.fetchone()

    if not selected:
        print("No recipe found with that ID.")
        return
    
    print("\nSelected recipe: ")
    item_id, name, ingredients, cooking_time, difficulty = selected
    
    print(f"\nID: {item_id}")
    print(f"Name: {name}")
    print(f"Ingredients: {ingredients}")
    print(f"Cooking Time: {cooking_time} minutes")
    print(f"Difficulty: {difficulty}")

    column = input("\nWhich field would you like to update? (name / ingredients / cooking_time): ").lower()

    if column not in ['name', 'ingredients', 'cooking_time']:
        print("Invalid column. PLease choose from name, ingredients, or cooking time")
        return
    new_value = input(f"Enter new value for {column}: ")

    if column in ['ingredients', 'cooking_time']:
            if column == 'ingredients':
                ingredients_list = new_value.split(", ")
                cooking_time = selected[3]
            else:
                ingredients_list = selected[2].split(", ")
                try:
                    cooking_time = int(new_value) 
                except ValueError:
                    print("coking time must be a number.")
                    return
            new_difficulty = calculate_difficulty(cooking_time, ingredients_list) 

            query = f"UPDATE recipes SET {column} = %s, difficulty = %s WHERE item_id = %s"        
            values = (new_value, new_difficulty, recipe_id)
    else:
        query = f"UPDATE recipes SET {column} = %s WHERE item_id = %s"
        values = (new_value, recipe_id)

    cursor.execute(query, values)
    conn.commit()
    
    cursor.execute("SELECT * FROM recipes WHERE item_id = %s", (recipe_id,))
    updated = cursor.fetchone()

    if updated:
        item_id, name, ingredients, cooking_time, difficulty = updated
        print("Great! Recipe updated successfully.")
        print(f"\nID: {item_id}")
        print(f"Name: {name}")
        print(f"Ingredients: {ingredients}")
        print(f"Cooking Time: {cooking_time} minutes")
        print(f"Difficulty: {difficulty}")   
        
    


def delete_recipe(conn, cursor):
    cursor.execute("SELECT item_id, name, ingredients, cooking_time, difficulty FROM recipes") 
    recipes = cursor.fetchall()

    if not recipes:
        print("Sorry, no recipe found with that name.")
        return
    
    print("\nAvailable recipes: ")
    for recipe in recipes:
        item_id, name, ingredients, cooking_time, difficulty = recipe
        print(f"\nID: {item_id}")
        print(f"Name: {name}")
        print(f"Ingredients: {ingredients}")
        print(f"Cooking Time: {cooking_time} minutes")
        print(f"Difficulty: {difficulty}")

    try:
        recipe_id = int(input("\nEnter the ID of the recipe you want to delete: "))
    except ValueError:
        print("Invalid ID. please enter a number.")
        return
    
    cursor.execute("SELECT * FROM recipes WHERE item_id = %s",(recipe_id,))
    selected = cursor.fetchone()

    if not selected:
        print("No recipe found with that ID.")
        return
    
    print("\nSelected recipe: ")
    item_id, name, ingredients, cooking_time, difficulty = selected
    
    print(f"\nID: {item_id}")
    print(f"Name: {name}")
    print(f"Ingredients: {ingredients}")
    print(f"Cooking Time: {cooking_time} minutes")
    print(f"Difficulty: {difficulty}")

    confirm = input("\nAre you sure you want to delete this recipe? ( yes /no): ").lower()
    if confirm != "yes":
        print("Delete cancelled.")
        return

    cursor.execute("DELETE FROM recipes WHERE item_id = %s", (recipe_id,))
    conn.commit()
    
    print("Recipe deleted successfuly. ")
    

def main_menu(conn, cursor):
    while True:
        print("\n")
        print("Main Menu")
        print("============================")
        print("\nWhat would you like to do?\n")
        print("1. Create a new recipe")
        print("2. Search for recipes by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit the program")
        print("\n")

        choice = input("Your choice: ")

        if choice =='1':
            create_recipe(conn, cursor)
    
        elif choice == '2':
            search_recipe(conn, cursor)

        elif choice == '3':
            update_recipe(conn, cursor)

        elif choice == '4':
            delete_recipe(conn, cursor)
    
        elif choice == '5':
            print("\n")
            print("Exiting the program...\n")
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice, please try again.")

main_menu(conn, cursor)

    
