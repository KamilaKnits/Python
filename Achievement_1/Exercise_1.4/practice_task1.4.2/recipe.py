import pickle

recipe = {
    'Name': 'Tea',
    'Ingredients': {'Tea leaves', 'Water', 'Sugar'},
    'Cooking Time': 5,
    'Difficulty': 'Easy'
}

my_file = open('recipe_binary.bin', 'wb')
pickle.dump(recipe, my_file)
my_file.close()

with open('recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print('Name: ' + recipe['Name'])
print('Ingredients: ' + str(recipe['Ingredients']))
print('Cooking Time: ' + str(recipe['Cooking Time']))
print('Difficulty: ' + recipe['Difficulty'])
   
