import unittest
import guess


class TestGame(unittest.TestCase):
    def test_input_correct_guess(self):
        guess.counter = 1
        guess_num = 5
        guess.number_to_guess = 5
        result = guess.is_guessed(guess_num)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        guess.counter = 1
        guess_num = 4
        guess.number_to_guess = 5
        result = guess.is_guessed(guess_num)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        guess.counter = 1
        guess_num = '4'
        guess.number_to_guess = 5
        result = guess.is_guessed(guess_num)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
