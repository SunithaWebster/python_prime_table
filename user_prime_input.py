def user_input():
    while True:
        try:
            number = int(input("Please enter your chosen positive integer: "))
            if number < 0:
                raise ValueError("You have not entered a positive number - please try again.")
        except ValueError:
            print("You have not entered an integer - please try again with a positive integer.")
            continue
        else:
            print("Thank you for your valid input.")
            break
    return number


user_input()
