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


def primes_boolean_list():
    max_number = 1000077
    prime = [True for i in range(max_number)]
    start = 2
    # Limit search to square root of list length
    while start * start <= max_number:
        # Sift out composites as per Sieve of Eratosthenes, using range step argument
        if prime[start]:
            for i in range(start * start, max_number, start):
                prime[i] = False
        start += 1
    return prime


def retrieve_primes_to_n():
    max_number = 1000077
    primes = []
    N = user_input()
    prime = primes_boolean_list()
    for start in range(2, max_number):
        if prime[start]:
            primes.append(start)
    primes_list = primes[:N]
    print(f"\nHere is a list of the first {N} prime(s): {primes_list}")
    return primes_list


def display_multiplication_table():
    primes = retrieve_primes_to_n()
    multi_table_products = []
    print("\nHere is the multiplication table:\n")
    print("|  | " + '| '.join(str(prime) for prime in primes), end='|\n')
    for i in primes:
        print("| " + str(i), end='|')
        for j in primes:
            print(" " + str(i * j), end='|')
            multi_table_products.append(i * j)
        print()
    return multi_table_products


if __name__ == '__main__':
    display_multiplication_table()
