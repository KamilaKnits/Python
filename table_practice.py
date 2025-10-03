import sqlalchemy
from sqlalchemy import create_engine, text, Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://cf-python:password@localhost/my_database")
Session = sessionmaker(bind=engine)
session = Session()

# alternative engine using myseql-connector-python:
#  engine = create_engine("mysql+mysqlconnector://cf-python:password@localhost/my_database")

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM recipes"))
#     for row in result:
#         print(row)

Base = sqlalchemy.orm.declarative_base()

#model; data model, it's a new class importing properties from Base
class Recipe(Base):
    __tablename__ = "practice1_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # helps identitfy objects easily from the terminal
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
# creates the tables of all models defined
Base.metadata.create_all(engine)

# tea = Recipe(
#     name = "Tea",
#     cooking_time = 5,
#     ingredients = "Tea Leaves, Water, Honey"
# )
# # add object to database
# session.add(tea)
# # commit entry
# session.commit()


# coffee = Recipe(
#     name = "Coffee",
#     cooking_time = 5,
#     ingredients = "Coffee Powder, Sugar, Water"
# )
# session.add(coffee)
# session.commit()

# cake = Recipe(
#     name = "Cake",
#     cooking_time = 50,
#     ingredients = "Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk"
# )
# session.add(cake)
# session.commit()

# banana_smoothie = Recipe(
#     name = "Banana Smoothie",
#     cooking_time = 5,
#     ingredients = "Bananas, Milk, Peanut Butter, Sugar, Ice Cubes"
# )
# session.add(banana_smoothie)
# session.commit()


# recipes_list = session.query(Recipe).all()
# for recipe in recipes_list:
#     print("Recipe ID: ",recipe.id)
#     print("Recipe Name: ", recipe.name)
#     print("Ingredients: ", recipe.ingredients)
#     print("Cooking Time: ", recipe.cooking_time)

# session.query(Recipe).get(1) deprecated; doesn't work
# retrieve one single object
# recipe = session.get(Recipe, 1)
# print(recipe)

# retrieving one or more objects using filter() method
# recipe = session.query(Recipe).filter(Recipe.ingredients.like("%Sugar%")).all()
# print(recipe)

# recipe = session.query(Recipe).filter(Recipe.ingredients.like("%Sugar%"), Recipe.ingredients.like("%Baking Powder%")).all()
# print(recipe)

# conditions_list = [
#     Recipe.ingredients.like("%Milk%"),
#     Recipe.ingredients.like("%Baking Powder%")    
# ]
# recipe = session.query(Recipe).filter(*conditions_list).all()

# Updating entries

# recipes_list = session.get(Recipe,1)
# recipes_list.ingredients  += ", Cardamon"
# print(recipes_list.ingredients)
# session.commit()

# recipes_list = session.get(Recipe,3)
# recipes_list.ingredients  += ", Chocolate Powder"
# print(recipes_list.ingredients)

# making direct changes using update() method

# recipe = session.query(Recipe).filter(Recipe.name =="Cake").update({Recipe.name: "Birthday Cake"})
# print(recipe)
# session.commit()

# updated_recipe = session.query(Recipe).filter(Recipe.name =="Birthday Cake").all()
# for recipe in updated_recipe:
#     print(recipe)

# deleting ojects from table

# buttered_toast = Recipe(
#     name = "Buttered Toast",
#     ingredients = "Bread, Butter",
#     cooking_time = 4
# )
# session.add(buttered_toast)
# session.commit()

# recipe_to_be_deleted = session.query(Recipe).filter(Recipe.name == "Buttered Toast").one()
# session.delete(recipe_to_be_deleted)
# session.commit()

recipe = session.query(Recipe.name).all()
print(recipe)

recipe = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
print(recipe)








    




