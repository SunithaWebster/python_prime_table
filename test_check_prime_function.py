#  A program to test if the prime checking function, check_prime, works
from unittest import TestCase, main
from check_prime_function import check_prime


class TestCheckPrime(TestCase):

    # This test should fail
    def test_check_prime(self):
        expected = check_prime()
        result = check_prime()
        self.assertEquals(expected, result)


if __name__ == 'main':
    main()
