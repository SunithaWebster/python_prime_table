#  A program to test if the make_primes_list function, retrieve_primes_to_n, works
from unittest import TestCase, main
from make_primes_list import retrieve_primes_to_n


class TestMakePrimesList(TestCase):

    def test_primes_boolean_list(self):
        primes_list = retrieve_primes_to_n()
        self.assertTrue(primes_list)


if __name__ == 'main':
    main()
