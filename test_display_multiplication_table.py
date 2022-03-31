#  A program to test if the make_primes_list function, display_multiplication_table, works
from unittest import TestCase, main
from make_primes_list import display_multiplication_table


class TestMakePrimesList(TestCase):

    # This test should fail
    def test_display_multiplication_table(self):
        multi_table = display_multiplication_table()
        expected = multi_table.primes[1] * multi_table.primes[0]
        result = multi_table.multi_table_products[3]
        self.assertNotEqual(expected, result)


if __name__ == 'main':
    main()
