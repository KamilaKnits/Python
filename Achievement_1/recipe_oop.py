class Recipe:
    all_ingredients = set()

    def __init__(self,name, ingredients, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    
    def add_ingredients(self, ingredients):
        for ingredient in ingredients:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
                self.update_all_ingredients(ingredient)
    
    def get_ingredients(self):
        return self.ingredients
    
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.ingredients) <= 4:
            self.difficulty = "Hard"
        
    
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self, ingredient):
        Recipe.all_ingredients.add(ingredient)
        
    
    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}\nCooking Time: {self.cooking_time} minutes\nDifficulty: {self.get.difficulty()}"

def recipe_search(data, search_term):  
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
    

Tea = Recipe("Tea", [], 5)
Tea.add_ingredients(["Tea leaves", "Sugar", "Water"])
print(Tea)


Coffee = Recipe("Coffee",[] , 5)
Coffee.add_ingredients(["Ground Coffee", "Sugar", "Water"])
print(Coffee)

Cake = Recipe("Cake", [], 50)
Cake.add_ingredients(["Sugar", "Butter", "Eggs", "Vanilla Essense", "Flour", "Baking Powder", "Milk"])
print(Cake)

Banana_Smoothie = Recipe("Banana_Smoothie", [], 5)
Banana_Smoothie.add_ingredients(["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"])
print(Banana_Smoothie)


recipes_list = [Tea, Coffee, Cake, Banana_Smoothie]

print("\nRecipes with Water: " )            
recipe_search(recipes_list,"Water")

print("\nRecipes with Sugar: " )            
recipe_search(recipes_list,"Sugar")

print("\nRecipes with Bananas: " )            
recipe_search(recipes_list,"Bananas")
