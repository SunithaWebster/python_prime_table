#  A program to test if the make_primes_list function, primes_boolean_list, works
from unittest import TestCase, main
from prime_table_app import primes_boolean_list


class TestMakePrimesList(TestCase):

    def test_primes_boolean_list(self):
        primes_bool = primes_boolean_list()
        expected = primes_bool
        result = not any(primes_bool)
        self.assertNotEqual(expected, result)


if __name__ == 'main':
    main()
