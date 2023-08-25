import unittest
from unittest.mock import patch, Mock
import game  # A Game Module Is Imported

# Create a new test class that inherits unittest.TestCase

class TestNumberGuessingGame(unittest.TestCase):

    # Test case for with valid input by the user
    @patch('builtins.input', side_effect=['1234'])
    def test_user_guess_num_valid_input(self, mock_input):
        result = game.user_guess_num()
        self.assertEqual(result, 1234)  # Verify that the function provides an accurate prediction.

    # Test case for various invalid guesses
    @patch('builtins.input', side_effect=['12', '12345', 'abc', 'q'])
    def test_user_guess_num_invalid_input(self, mock_input):
        results = []
        with patch('builtins.print') as mock_print:
            for _ in range(4):
                try:
                    results.append(game.user_guess_num())  # Compile the responses to function calls.
                except SystemExit:
                    pass
        self.assertEqual(results, [None, None, None, None])  # Verify if the result of an invalid input is returned None
        mock_print.assert_called()  # Perform a print check to see if the error message appeared.

    # Test case for exact match of guessed number
    def test_compare_random_num_exact_match(self):
        random_num = [1, 2, 3, 4]
        result = game.compare_random_num(random_num, 1234)
        self.assertEqual(result, 'oooo')  # Check if the exact match is correctly detected

    # Test case for the partial match of the guessed number
    def test_compare_random_num_partial_match(self):
        random_num = [1, 2, 3, 4]
        result = game.compare_random_num(random_num, 1423)
        self.assertEqual(result, 'oxxx')  # to Verify that a partial match has been successfully detected.

    # Test case for no match of the guessed number
    def test_compare_random_num_no_match(self):
        random_num = [1, 2, 3, 4]
        result = game.compare_random_num(random_num, 5678)
        self.assertEqual(result, '____')  # Verify that there is no detected match.

    # Test case for player game win
    @patch('game.generate_random_num', return_value=[1, 2, 3, 4])
    @patch('builtins.input', side_effect=['1234', 'q'])
    def test_game_win(self, mock_input, mock_generate_random_num):
        num_of_attempts = game.game()
        self.assertEqual(num_of_attempts, 1)  # Verify that the correct number of attempts were made to declare victory.

    # Test case for the player loses
    @patch('game.generate_random_num', return_value=[1, 2, 3, 4])
    @patch('builtins.input', side_effect=['5678', 'q'])
    def test_game_lose(self, mock_input, mock_generate_random_num):
        num_of_attempts = game.game()
        self.assertEqual(num_of_attempts, 2)  # Check the failure rate by verifying the actual number of attempts


# When the script has been executed, immediately begin testing.
if __name__ == '__main__':
    unittest.main()
