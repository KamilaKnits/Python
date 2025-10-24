# Task 2.5 Recipe Model Changes

## Recipe Model in Exercise 2.3

- 'recipe_id' Primary Key
- 'name' Recipe Name
- 'ingredients' Comma separated ingredients
- 'cooking_time' Cooking time in minutes
- 'difficulty' Difficulty level

## Changes to the Recipe Model

1. New Fields Added

- 'recipe_image' Picture of recipe
- 'recipe_description' Quick description of the recipe


The image of the recipe makes the recipe more inviting. The recipe summary gives the user an idea about the recipe. It helps to have a description to know what to expect.

2. Fields Altered

- 'difficulty' Difficulty level

Made more sense to have it autocalculated to make it uniform. 

## New Recipe Model

- 'recipe_id' Primary Key
- 'name' Recipe Name
- 'recipe_description' Short description of the recipe
- 'ingredients' Comma separated ingredients
- 'cooking_time' Cooking time in minutes
- 'difficulty' Difficulty level
- 'recipe_image' Picture of the recipe

## Frontend inspirations

https://www.pinterest.com/

- Love the tile layout and the clean feel of it. I would like to reproduce the responsive image gallery on my recipe-list page.

https://www.paprikaapp.com/

- Has a similar layout and I like the rating of each recipe. Perhaps I can add this feature eventually.


https://varecha.pravda.sk/recepty/

- Like the category of recipes at the top of the main page
- There is a section that shows what other users have clicked on in the past day, week and month. 
- Concept seems a bit advanced but would be fun to implement trending recipes to my app.  


