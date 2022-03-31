#  A program to test if the make_primes_list function, display_multiplication_table, works
from unittest import TestCase, main
from prime_table_app import display_multiplication_table, retrieve_primes_to_n


class TestMakePrimesList(TestCase):

    def test_display_multiplication_table(self):
        multi_table = display_multiplication_table()
        primes = retrieve_primes_to_n()
        expected = primes[1] * primes[0]
        result = multi_table[3]
        self.assertNotEqual(expected, result)


if __name__ == 'main':
    main()
