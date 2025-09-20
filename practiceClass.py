# Class example; changing values without setter getter methods

# class Date(object):
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

# first_moon_landing = Date(20,7,1969)

# print("initial values in first_moon_landing")
# print(first_moon_landing.day)
# print(first_moon_landing.month)
# print(first_moon_landing.year)

# first_moon_landing.day = 25
# first_moon_landing.month = 11
# first_moon_landing.year = 1800

# print()
# print("Modified values in first_moon_landing")
# print(first_moon_landing.day)
# print(first_moon_landing.month)
# print(first_moon_landing.year)

# setter and getter methods

# class Date(object):
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     # getter method; gets, retrives the value of an object
#     def get_date(self):
#         output = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
#         return output
    
#     #setter method: sets, modifies the value of an object
#     def set_date(self):
#         self.date = int(input("Enter the day of the month: "))
#         self.month = int(input("Enter the month: "))
#         self.year = int(input("Enter the year: "))
    
# first_moon_landing = Date (20,7,1969)

# print(first_moon_landing.get_date())

# first_moon_landing.set_date()

# print(first_moon_landing.get_date())


# class Date(object):
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def get_date(self):
#         output = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
#         return output

#     def is_leap_year(self):
#         return self.year % 4 == 0
    
#     def is_valid_date(self):
#         # first check if the values are all integers
#         if not (type(self.day) == int and type(self.month) == int and type(self.year == int)):
#             return False
        
#         # then make sure that the year isn't negative
#         if self.year < 0:
#             return False
        
#         # after this we check if the given month is between 1 and 12
#         if self.month < 1 or self.month > 12:
#             return False    
        
#         # then verify if the day is valid for a given month. list out the dates for 
#         # each month in a dictionary - keys are months, values are number of days in 
#         # corresponding months
#         last_dates = {
#             1: 31,
#             2: 29 if self.is_leap_year() else 28,
#             3: 31,
#             4: 30,
#             5: 31,
#             6: 30,
#             7: 31,
#             8: 31,
#             9: 30,
#             10: 31,
#             11: 30,
#             12: 31
#         }

#         # verify that the date is valid for the given month
#         if self.day < 1 or self.day > last_dates.get(self.month):
#             return False
    
#         # if none of the above if statements triggered the 'return False' statements
#         # then the script reaches this point where it is True
#         return True

# # initializing a few date objects with some of them having erroneous values

# # this one valid; a leap year
# date1 = Date(29, 2, 2000)

# # this one invalid since not a leap year
# date2 = Date(29, 2, 2001)

# # this one invalid since values not int
# date3 = Date('abc', 'def', 'ghi')


# print(str(date1.get_date()) + ": " + str(date1.is_valid_date()))
# print(str(date2.get_date()) + ": " + str(date2.is_valid_date()))
# print(str(date3.get_date()) + ": " + str(date3.is_valid_date()))


#polymorphism
# define class
# class Cow(object):
#     def speak(self):
#         print("moooooooo")
        

# class Dog(object):
#     def speak(self):
#         print("woooooof")
        

# # generate object from each class (initialize an object)
# cow = Cow()
# dog = Dog()

# # #invoke speak method from each object
# cow.speak()
# dog.speak()

# calling method directly from a Class
# class Date(object):
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
    
#     def get_date(self):
#         output = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
#         return output

# # # initialized an object
# date = Date(1,1,2025)

# # # calling the 'get_date' from the class itself. Passing the obejct 'date' through
# # # the 'self' argument.
# print(Date.get_date(date))

# using a method to interact between multiple objects
# class ShoppingList:
#     # initialization method
#     def __init__(self, list_name):
#         self.list_name = list_name
#         self.shopping_list = []

#     # method to add new items to self.shopping_list
#     def add_item(self, item):
#         # simple filter to avoid repeated items
#         if not item in self.shopping_list:
#             self.shopping_list.append(item)

#     # method to remove item from self_shopping_list. use Try -ecxept block
#     # to avoid errors in case item not found
#     def remove_item(self, item):
#         try:
#             self.shopping_list.remove(item)
#         except:
#             print("Item not found.")
    
#     # method to view shopping list
#     def view_list(self):
#         print("\nItems in " + str(self.list_name) + "\n" + 30*"_")
#         for item in self.shopping_list:
#             print(" - " + str(item))

#     def merge_lists(self, obj):
#         # creating a name for our new. merged shopping list
#         merged_lists_name = 'Merged List - ' + str(self.list_name) + " + " + str(obj.list_name)

#         # creating an empty ShoppingList object 
#         merged_lists_obj = ShoppingList(merged_lists_name)

#         # adding the first shopping lists's item to our new list
#         merged_lists_obj.shopping_list = self.shopping_list.copy()

#         # adding the second shopping list's items to our new list - so there won't be
#         # any repeated items in the final list if both lists contain common items
#         for item in obj.shopping_list:
#             if not item in merged_lists_obj.shopping_list:
#                 merged_lists_obj.shopping_list.append(item)
        
#         # return our new merged object
#         return merged_lists_obj
    
# pet_store_list = ShoppingList("Pet Store List")
# grocery_store_list = ShoppingList("Grocery Store List")

# for item in ["dog", "frisbee", "bowl", "collars", "flea collars"]:
#     pet_store_list.add_item(item)

# for item in ["fruits", "vegetables", "bowl", "ice cream"]:
#     grocery_store_list.add_item(item)

# merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

# merged_list.view_list()

# String representation of an Object
# class Height(object):
#     def __init__(self, feet, inches):
#         self.feet = feet
#         self.inches = inches

#     def __str__(self):
#         output = str(self.feet) + " feet," + str(self.inches) + " inches"
#         return output

# Adam = Height(5, 10)
# print(Adam)

# addition and subtraction of an Object
# class Height(object):
#     def __init__(self, feet, inches):
#         self.feet = feet
#         self.inches = inches

#     def __str__(self):
#         output = str(self.feet) + " feet," + str(self.inches) + " inches"
#         return output
    
#     def __add__(self, other):
        
#         # converting both object's height into inches
#         height_A_inches = self.feet * 12 + self.inches
#         height_B_inches = other.feet * 12 + other.inches

#         # adding them up
#         total_height_inches = height_A_inches + height_B_inches

#         # getting the output in feet
#         output_feet = total_height_inches // 12

#         # getting output in inches
#         output_inches = total_height_inches - (output_feet * 12)

#         # returning the final output as a new Height object
#         return Height(output_feet, output_inches)
    
# person_A_height = Height(5, 10)
# person_B_height = Height(4, 10)
# height_sum = person_A_height + person_B_height

# print("Total Height:", height_sum)

# class Height(object):
#     def __init__(self, feet, inches):
#         self.feet = feet
#         self.inches = inches

#     def __str__(self):
#         output = str(self.feet) + " feet," + str(self.inches) + " inches"
#         return output
    
#     def __sub__(self, other): 
#         # converting both object's height into inches
#         height_A_inches = self.feet * 12 + self.inches
#         height_2_sub = other.feet * 12 + other.inches

#         # subtracting them
#         total_height_inches = height_A_inches - height_2_sub

#         #getting the output in feet
#         output_feet = total_height_inches // 12

#         # getting the output in inches
#         output_inches = total_height_inches - (output_feet * 12)

#         #returning final output as new Height object
#         return Height(output_feet,output_inches)

# person_A_height = Height(5,10)
# amount_2_sub = Height(3,9)
# height_sub = person_A_height - amount_2_sub

# print("New Height: ", height_sub)

# class Height(object):
#     def __init__(self, feet, inches):
#         self.feet = feet
#         self.inches = inches

#     def __str__(self):
#         output = str(self.feet) + " feet," + str(self.inches) + " inches"
#         return output
    
#     def __lt__(self, other):
#         height_inches_A = self.feet * 12 + self.inches
#         height_inches_B = other.feet * 12 + other.inches
#         return height_inches_A < height_inches_B
    
#     def __le__(self, other):
#         height_inches_A = self.feet * 12 + self.inches
#         height_inches_B = other.feet * 12 + other.inches
#         return height_inches_A <= height_inches_B
    
#     def __eq__(self, other):
#         height_inches_A = self.feet * 12 + self.inches
#         height_inches_B = other.feet * 12 + other.inches
#         return height_inches_A == height_inches_B
    
#     def __gt__(self, other):
#         height_inches_A = self.feet * 12 + self.inches
#         height_inches_B = other.feet * 12 + other.inches
#         return height_inches_A > height_inches_B
    
#     def __ge__(self, other):
#         height_inches_A = self.feet * 12 + self.inches
#         height_inches_B = other.feet * 12 + other.inches
#         return height_inches_A >= height_inches_B
    
#     def __ne__(self, other):
#         height_inches_A = self.feet * 12 + self.inches
#         height_inches_B = other.feet * 12 + other.inches
#         return height_inches_A != height_inches_B
    
# person_A_height = Height(4,5)
# person_B_height = Height(4,6)

# height_less_than = person_A_height < person_B_height
# print(height_less_than)

# height_less_or_equal = person_A_height <= person_B_height
# print(height_less_or_equal)

# height_equal = person_A_height == person_B_height
# print(height_equal)

# making a class sortable
# height_1 = Height(4,10)
# height_2 = Height(5,6)
# height_3 = Height(7,1)
# height_4 = Height(5,5)
# height_5 = Height(6,7)
# height_6 = Height(5,6)

# heights = [height_1, height_2, height_3 ,height_4, height_5, height_6]

# heights = sorted(heights)
# for height in heights:
#     print(height)

# heights = sorted(heights, reverse=True)
# for height in heights:
#     print(heights) 




# Inheritance
# parent class
# class Person:
#     def walk():
#         print("hello, i can walk")

# # inherited class or subclass
# class Athlete(Person):
#     def run():
#         print("hey, i can run too")




class Animal(object):
    # every animal has an age, but a name may not be necessary

    def __init__(self, age):
        self.age = age
        self.name = None

    # getter methods for age and name
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    # and setter methods as well
    def set_age(self, age):
        self.age = age
    
    def set_name(self, name):
        self.name = name
    
    # not a well-formatted string representation too
    def __str__(self):
        output = "\nClass: Animal\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output

a = Animal(5)
print(a)

class Cat(Animal):
    # introducing new method where it speaks
    def speak(self):
        print("meow")

    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output

class Dog(Animal):
    # implementing another speak method but for dogs
    def speak(self):
        print("woof")

    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output

cat = Cat(3)
dog = Dog(6)

cat.set_name("stripes")
dog.set_name("bubbles")

print(cat)
print(dog)

cat.speak()
dog.speak()

class Human(Animal):
    # it's own initialization method
    def __init__(self, name, age):
    
        # calling the parent class init method to initialize other attributes like 
        # name and age
        Animal.__init__(self, age)

        # setting a name
        self.set_name(name)

        # new attribute added
        self.friends = []

    # adding another method to add friends
    def add_friend(self, friend_name):
        self.friends.append(friend_name)
    
    # a method to display friends
    def show_friends(self):
        for friend in self.friends:
            print(friend)
    
    # a method to speak
    def speak(self):
        print("hello, my name is " + self.name + "!")
    
    # a method to modify the string representation
    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + \
            "\nAge: " + str(self.age) + "\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
        return output
    
human = Human("tobias", 35)

human.add_friend("Robert")
human.add_friend("Élise")
human.add_friend("Abdullah")
human.add_friend("Asha")
human.add_friend("Lupita")
human.add_friend("Saito")

human.speak()
print(human)


#Class variables
class Example(object):
    common_string = "Hello, I can be accessed from anywhere!"
    def __init__(self,a,b):
        self.a = a
        self.b = b

# initialize 2 objects
alpha = Example(1,2)
beta = Example(3,4)

alpha.common_string
beta.common_string
Example.common_string
Example.common_string = "I've changed"


class Car(object):
    id = 0
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.id = Car.id
        Car.id += 1
    
    def __str__(self):
        output = "\nID: " + str(self.id) + \
            "\nName: " + self.name + \
            "\nModel: " + self.model + \
            "\nYear: " + self.year
        return output

c0 = Car("Ford", "Shelby GT500", "2015")
c1 = Car("Toyota", "Corolla", "2012")
c2 = Car("BMW", "Z3", "2001")
c3 = Car("Audi", "A6", "2020")

print(c0)
print(c1)
print(c2)
print(c3)

