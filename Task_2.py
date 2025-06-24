"""
Programming Task #2
TASK
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was "lower" or "higher" than the target number.

Note that you will need to use the random library's randint function.

How it works:

Why it works:

"""

import random

def generate_random_number():
    """
    Generate a random integer between 1 and 100 (include 1 and 100).
    
    Returns:
        int: a random integer between 1 and 100
    """
    return random.randint(1, 100)

def display_welcome_message():
    """
    Display game's welcome message and instruction.
    """
    print("Welcome to the game!!!")
    print("I'm thinking of a number.")
    print("Can you guess what it is? It's between 1 and 100, inculed 1 and 100.")
    print("I'll tell you if you need to go higher or lower." + "\n")

def get_user_guess():
    """
    Ask user for an valid integer, between 1 and 100, include 1 and 100.
    Check for invalid inputs, notifying the user and re-prompting for a valid input.

    Returns:
        int: a valid integer between 1 and 100
    """
    while True:
        try:
            # Get input from user
            user_input = input("Please enter your guess: ")
            # Try to convert to integer
            guess = int(user_input)
            # Check if the integer is in the validate range
            if guess < 1 or guess > 100:
                print("Please enter a integer between 1 and 100.")
                # Back to ask for user_input
                continue
            return guess
        # Handle non-integer input
        except ValueError:
            print(f"{user_input} is not a valid number.Please enter a integer.")

def check_guess(guess, target):
    """
    Compare the user's guess to the target number.

    Args:
        guess(int): The user's guess.
        target(int): The target number for user to guess.

    Returns:
        str: 'higher', 'lower', or 'correct' depending on the guess.
    """
    if guess < target:
        return "highter"
    elif guess > target:
        return "lower"
    else:
        return "correct"
    
def ask_play_again():
    """
    Ask the user if they want to play again.

    Returns:
        bool: True (user wants to play again), False (user don't wants to play again)
    """
    while True:
        response = input("Would you like to play again? (yes/no): ").lower().strip()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")
    
def main_game():
    """
    Main function to run the number guessing game.
    """
    while True:
        display_welcome_message()

        target = generate_random_number()
    
        while True:
            guess = get_user_guess()

            result = check_guess(guess, target)

            if result == "highter":
                print("Try a highter number.")
            elif result == "lower":
                print("Try a lower number.")
            else:
                print(f"Congratulations! You've got the right number!")
                break
        if not ask_play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main_game()