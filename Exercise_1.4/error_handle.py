def divide():

    try:
        a = int(input("Enter a number to be divided: "))
        b = int(input("Enter another number to divide it by: "))
        result = a/b

    except ValueError:
        print("One or more of your inputs are not numbers.")
        return None

    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    
    except:
        print("oops, we have stumbled on some unexpected error.")
        return None
    else:
        return result

    finally:
        print("Function complete")

print("Result: " + str(divide()))
 