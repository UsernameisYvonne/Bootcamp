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
    