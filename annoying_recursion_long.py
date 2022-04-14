"""
File: annoying_recursion_long.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Long Project 5, Annoying Recursion
"""

def annoying_fibonacci_sequence(n):
    """
    Outputs a fibonacci sequence given an input. The list structure containing
    the values is built via recursion.

    Parameters:
        n: an integer
    """
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n == 3:
        return [0, 1, 1]
    else:
        if n == 4:
            new_sequence = annoying_fibonacci_sequence(3)
            next_in_sequence = sum(annoying_fibonacci_sequence(3)[-2:])
            new_sequence.append(next_in_sequence)
            return new_sequence
        if n == 5:
            new_sequence = annoying_fibonacci_sequence(4)
            next_in_sequence = sum(annoying_fibonacci_sequence(4)[-2:])
            new_sequence.append(next_in_sequence)
            return new_sequence
        if n == 6:
            new_sequence = annoying_fibonacci_sequence(5)
            next_in_sequence = sum(annoying_fibonacci_sequence(5)[-2:])
            new_sequence.append(next_in_sequence)
            return new_sequence
        else:
            new_sequence = annoying_fibonacci_sequence(n-1)
            next_in_sequence = sum(annoying_fibonacci_sequence(n-1)[-2:])
            new_sequence.append(next_in_sequence)
            return new_sequence