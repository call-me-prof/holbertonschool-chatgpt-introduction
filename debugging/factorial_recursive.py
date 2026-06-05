#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): The number to compute the factorial for.

    Returns:
    int: The factorial of the number n, or 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
