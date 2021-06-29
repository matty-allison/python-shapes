try:
    x = int(input("please enter a number: "))
except ZeroDivisionError:
    print("you can not divide by 0")
except ValueError:
    print("Please enter a valid integer")
