first_value = int(input("Enter a number: "))
second_value = int(input("Enter another number: "))
third_value = input("Enter a + to add or a - to subtract: ")

if third_value == "+":
    print(first_value + second_value)

elif third_value == "-":
    print(first_value - second_value)

else:
    print("Unknown operator")