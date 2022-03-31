from user_prime_input import user_input


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
