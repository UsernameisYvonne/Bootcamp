"""
Programming Task #2
TASK
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was "lower" or "higher" than the target number.

Note that you will need to use the random library's randint function.

How it works:
1. The computer generates a random number between 1 and 100 (include 1 and 100)
2. The user enters their guess
3. The program compares the guess with target number
4. (1) If the guess is lower than target, it tells user to go "heigher"
   (2) If the guess is heigher than target, it tells user to go "lower"
5. Repeat steps 2-4, until the user got teh correct guess
6. After one round of the game is complited, ask if teh user wants to play again or exit

Why it works:
This game uses a feedback loop to guide the user toward the right answer.
And give feedback (need to go highter or lower) each time after user entered a guess.
After one round of the game is complited, the game will ask the user if they would like to play again or not.
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
        return "higher"
    elif guess > target:
        return "lower"
    else:
        return "correct"
    
def display_hint_message(result):
    """
    Display an hint massage for user to adjust their guess.

    Args:
        str(result): The result from check_guess ("higher" or "lower") 
    """
    if result == "higher":
        print("Try a higher number.")
    elif result == "lower":
        print("Try a lower number.")

def display_victory_message(attempts):
    """
    Display a congratulatory message when the user wins.

    Args:
        int(attempts): Number of attempts it took to guess correctly
    """
    # Provide feedback for user based on attempts number
    if attempts == 1:
        print(f"WOW!!!Unbelievable! You've got the right number in only 1 attempt!!")
    else:
        print(f"Congratulations! You've got the right number in {attempts} attempts!")

def one_round():
    """
    One complete round of the guessing game.

    Returns:
        int(attempts): The number of attempts it took to guess correctly
    """
    # Generate the target number
    target = generate_random_number()
    # Start attempts number at 0, and track it
    attempts = 0

    # Game loop for one round
    while True:
        # Get user's guess
        guess = get_user_guess()
        attempts += 1
        # Check the guess
        result = check_guess(guess, target)
        # Handle the result
        if result == "correct":
            return attempts
        else:
            display_hint_message(result)
    
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
    Manages multiple rounds and the overall game flow.
    """
    # Display welcome message
    display_welcome_message()

    # Main game loop
    while True:
        # Play one round and get the number of attempts
        attempts = one_round()
        # Display victory massage
        display_victory_message(attempts)
        # Ask if the user wants to play again
        if not ask_play_again():
            print("\n" + "Thank you for playing! Goodbye!")
            # Exit outer loop if user says 'no'
            break
        else:
            print("\n" + "A new game is starting...")

if __name__ == "__main__":
    main_game()