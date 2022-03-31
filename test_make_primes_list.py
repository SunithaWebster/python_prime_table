#  A program to test if the make_primes_list function, primes_boolean_list, works
from unittest import TestCase, main
from make_primes_list import primes_boolean_list


class TestMakePrimesList(TestCase):

    # This test should fail
    def test_primes_boolean_list(self):
        primes_bool = primes_boolean_list()
        expected = primes_bool
        result = not any(primes_bool)
        self.assertEqual(expected, result)


if __name__ == 'main':
    main()
