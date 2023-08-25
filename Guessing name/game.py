import random

# Creates a random number between 0 and 9 in a set of four digits.
def generate_random_num():
    return [random.randint(0, 9) for _ in range(4)]

# User-guessing input function
def user_guess_num():
    while True:
        users_guess = input("Please enter your guess in the form of a four-digit number or type 'q' to terminate the game: ")

        if users_guess.lower() == 'q':
            return None
        try:
            if len(users_guess) != 4:
                raise ValueError
            users_guess = int(users_guess)  # Convert user input to integer
            return users_guess
        except ValueError:
            print("The input provided is not valid. Please input a four-digit number or 'q' to terminate the game.")
            return None  # Return None indicates an incorrect input.

# test a user's guess against a generated random number
def compare_random_num(randomly_generated_num, users_guess):
    hints = []
    users_guess_digits = [int(digit) for digit in str(users_guess)]  # Make a user's guess into a string of numbers.
    
    for i in range(4):
        if users_guess_digits[i] == randomly_generated_num[i]:
            hints.append('o')  # hint if the guessed number is exact match
        elif users_guess_digits[i] in randomly_generated_num:
            hints.append('x')  # hint if the number present but in a different position
        else:
            hints.append('_')  # hint if the guessed number doesnot match 
    
    return ''.join(hints)

# Main game loop
def game():
    randomly_generated_num = generate_random_num()  # Generate the random numbers to guess

    num_of_attempts = 0  # Number of Attempts Counter

    while True:
        num_of_attempts += 1
        users_guess = user_guess_num()  # guess of number from the user.

        
        if users_guess is None:
            print("Terminating the game.")
            break
        
        hints = compare_random_num(randomly_generated_num, users_guess)  # Compare guesses with the random generated number
        print(f"Hints: {hints}")
        
        if hints == "oooo":
            print(f" Congratulations! You nailed the correct digit{users_guess} in {num_of_attempts} attempts.")
            break  # if the user guess is correct exit the game

    return num_of_attempts  # Return the number of attempts by user to guess the number


def Guess_the_Number_game():# Start and restart game functionality.
    while True:
        print("Welcome to the Number Guessing Game!")
        num_of_attempts = game()  # Starting the game again
        
        users_choice = input("Would you like to play again? (y/n): ")
        if users_choice.lower() != 'y':
            print("What a fun game, Thankyou for participating!")
            break  # Exit the game if the player doesn't want to continue with the guessing game
        else:
            print("Restarting the game once again...\n")

# Point of entry into the game
if __name__ == "__main__":
    Guess_the_Number_game()  # Initiate the main game loop.

