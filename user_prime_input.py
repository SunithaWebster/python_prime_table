def user_input():
    while True:
        number = int(input("\nPlease enter your chosen positive integer, in digits: "))
        try:
            if number <= 0:
                raise ValueError
        except ValueError:
            print("\nZero or less are not valid inputs - please try again with a positive integer.")
            continue
        else:
            print("\nThank you for your valid input.")
            break
    return number
