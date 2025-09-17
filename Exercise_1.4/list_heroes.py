# def display(file):
#     heroes = []
#     for line in file:
#         # removes newline characters
#         line = line.rsrtip("\n")
#         # split('\n') used to split the hero name and the year separately.
#         # the separation occurs at ', '.
#         # taking the 1st element fo the split
#         hero_name = line.split(", ")[0]
#         #taking the 2nd element of the split
#         first_appearance = line.split(", ")[1]

#         # pack these two into smaller, two element list and then append them
#         # to the list "heroes"
#         heroes.append([hero_name, first_appearance])     

#     # this sorts 'heroes by first appearance
#     heroes.sort(key = lambda hero: hero[1])

#     for hero in heroes:
#         print("__________________________")
#         print("Superhero: " + hero[0])
#         print("First year of appearance: " + hero[1])    

# filename = input("Enter the filename where you have stored your heroes: ") 
# try:
#     file = open(filename, 'r')
#     display(file)

# except FileNotFoundError:
#     print("File does not exist - bummer")

# except:
#     print("An unexpected error occured.")
# else:
#     file.close()
# finally:
#     print("see yah!")

    
def display(file):
    heroes = []
    for line in file:
        # Removing newline characters
        line = line.rstrip("\n")

        # Here, we use the split(", ") method available to strings
        # to split the hero name and the year separately.
        # The separation occurs at ", ".

        # Taking the first element of the split
        hero_name = line.split(", ")[0]
        # Taking the second element of the split
        first_appearance = line.split(", ")[1]

        # We pack these two into a smaller, two-element
        # list, and then append it to the list "heroes".
        heroes.append([hero_name, first_appearance])

    # Now, we'll sort "heroes" by first appearance.
    heroes.sort(key = lambda hero: hero[1])

    for hero in heroes:
        print("--------------------------------------")
        print("Superhero: " + hero[0])
        print("First year of appearance: " + hero[1])




filename = input("Enter the filename where you've stored your superheroes: ")
try:
    file = open(filename, 'r')
    display(file)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
except:
    print("An unexpected error occurred.")
else:
    file.close()
finally:
    print("Goodbye!")