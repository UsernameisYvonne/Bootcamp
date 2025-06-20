"""
Programming Task #1
TASK
Given a list of digits, determine the integer that it represents.
For example, given the list: [8,3,5,1], your program should output 8351 as an integer.

What this program does:
This program takes a list of digits, like [8, 3, 5, 1], and determine the integer they represent, 
in this case, 8351.

How it works:
For every new list, the result always starts with 0.
- Multiply the current result by 10, this shifts the digit to the left.
- Add the new digit to the result.
Repeat until all digits in the list has been processed.

Why it works:
It's just like typing a number into a computer (like 288):
1. First you press 2 -> screen shows: 2
2. Then you press 8 -> screen shows: 28 (the 2 moved to the tens place)
3. Then you press 8 -> screen shows: 288 (the 28 moved left again)
"""

def convert_digit_list_into_integer(digit_list):
    """
    Convert a list of digits into the integer they represent.

    This function simulates how we usually construct multi-digit numbers:
    Shifting digits left and adding new digits on the right.

    Args:
        digit_list (list): A list of integers, each between 0-9, representing single digits.

    Returns:
        int: The integer formed by the digit list.
    """
    # Initialize the result to 0 (the number building starts here)
    result = 0

    # Process each and every digit in the list from left to right, one by one
    for digit in digit_list:
        # Multiply the current result by 10, shift all digits one place left (make room for the new digit)
        result = result * 10
        # Add the current digit to the ones place
        result = result + digit

        # For example:
        # digit_list = [8, 3, 5, 1]
        # result = 0
        # digit = 8 -> result = 0 * 10 = 0 -> result = 0 + 8 = 8
        # digit = 3 -> result = 8 * 10 = 80 -> result = 80 + 3 = 83
        # digit = 5 -> result = 83 * 10 = 830 -> result = 830 + 5 = 835
        # digit = 1 -> result = 835 * 10 = 8350 -> result = 8350 + 1 = 8351
        # result = 8351

    return result

# Test the function with some examples
if __name__ == "__main__":
    print(convert_digit_list_into_integer([9, 9, 9]))    # 999
    print(convert_digit_list_into_integer([3, 1, 0, 9])) # 3109
    print(convert_digit_list_into_integer([1, 0, 7]))    # 107
    print(convert_digit_list_into_integer([0, 1, 3]))    # 13
    print(convert_digit_list_into_integer([0]))          # 0