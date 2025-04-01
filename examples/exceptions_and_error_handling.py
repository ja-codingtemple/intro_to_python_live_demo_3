try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except Exception as error:
    print("An error has been encountered: " + error)