# Task 2.7 Data Analysis and Visualization in Django

## Data Analysis

What to search for? 

-Recipe by name
-Recipe by ingredient
-Recipe by cooking time

Criterion for search...
-'recipe_name'
-'ingredients'
-'cooking_time'
-'difficulty_level'
-'chart_type'

Format of output...

-table using Django template; table will show recipe id, name, ingredients, cooking time and difficulty.
-recipe name will be clickable and redirect to recipe detail view
-chart using Dataframes; user can pick between bar, pie, plot chart

### Bar Chart 

"Cooking Time by Recipe"
x-axis Recipe Name
y-axis Cooking Time (minutes)


### Pie Chart

"Difficulty"
labels = "Easy", "Medium", "Intermediate", "Hard",


### Plot Chart

"Cooking Time vs Difficulty"
x-axis Cooking Time (minutes)
y-axis Difficulty Level

## Execution Flow

1. Welcome page
2. Login page
3. Recipe List View
4. Recipe Search View
5. Recipe Detail View
6. Logout View
