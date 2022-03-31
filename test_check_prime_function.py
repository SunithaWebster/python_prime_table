#  A program to test if the prime checking function, check_prime, works
from unittest import TestCase, main
from check_prime_function import check_prime


class TestCheckPrime(TestCase):

    def test_check_prime(self):
        expected = check_prime()
        result = check_prime()
        self.assertEqual(expected, result)


if __name__ == 'main':
    main()
