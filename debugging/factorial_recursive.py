#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given integer.

    Parameters:
    - n: Integer representing the number for which factorial is to be calculated.

    Returns:
    Integer representing the factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
