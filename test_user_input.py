#  A program to test user input
from unittest import TestCase, main
from python_prime_table import user_input


class TestUserInput(TestCase):

    # This test should fail
    def test_user_input(self):
        expected = 5
        result = user_input("h")
        self.assertEquals(expected, result)


if __name__ == 'main':
    main()
