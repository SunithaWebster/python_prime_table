from user_prime_input import user_input


def check_prime():
    N = user_input()
    # Eliminating corner cases, 1 and 0
    if N <= 1:
        return False
    # Ensuring 2, 3 and 5 are identified as primes and not eliminated in next step
    elif (N <= 3) | (N == 5):
        return True
    # Eliminating multiples of 2, 3 and 5 as common composites, as per Sieve of Eratosthenes
    elif (N % 2 == 0) | (N % 3 == 0) | (N % 5 == 0):
        return False
    i = 5
    # Limiting loop to i, where i is the square root of N
    while i * i <= N:
        if (N % i == 0) | (N % (i + 2) == 0):
            return False
        i = i + 6
    return True
