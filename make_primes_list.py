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
