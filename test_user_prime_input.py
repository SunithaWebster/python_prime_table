#  A program to test user input
from unittest import TestCase, main
from user_prime_input import user_input


class TestUserPrimeInput(TestCase):

    # This test should fail
    def test_user_input(self):
        expected = user_input()
        result = user_input()
        self.assertEquals(expected, result)


if __name__ == 'main':
    main()
