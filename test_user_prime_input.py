#  A program to test user input
from unittest import TestCase, main
from make_primes_list import user_input


class TestUserPrimeInput(TestCase):

    def test_user_input(self):
        expected = user_input()
        result = user_input()
        self.assertEqual(expected, result)


if __name__ == 'main':
    main()
