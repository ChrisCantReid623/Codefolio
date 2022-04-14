"""
File: annoying_recursion_short.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Short PA # 7
"""

def annoying_factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    else:
        if n == 4:
            return 4 * annoying_factorial(3)
        elif n == 5:
            return 5 * annoying_factorial(4)
        elif n == 6:
            return 6 * annoying_factorial(5)
        else:
            return n * annoying_factorial(n - 1)

def annoying_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        if n == 4:
            return annoying_fibonacci(3) + annoying_fibonacci(2)
        elif n == 5:
            return annoying_fibonacci(4) + annoying_fibonacci(3)
        elif n == 6:
            return annoying_fibonacci(5) + annoying_fibonacci(4)
        else:
            return annoying_fibonacci(n - 1) + annoying_fibonacci(n - 2)

def annoying_very_quizzical(n):
    if n == 0:
        return 'what'
    elif n == 1:
        return 'what?'
    elif n == 2:
        return 'what?!'
    elif n == 3:
        return 'what?!?'
    else:
        if n == 4:
            return 'what?!?!'
        elif n == 5:
            return 'what?!?!?'
        elif n == 6:
            return 'what?!?!?!'
        else:
            if n % 2 == 1:
                return annoying_very_quizzical(n - 1) + '?'
            elif n % 2 == 0:
                return annoying_very_quizzical(n - 1) + '!'

def annoying_parens(n):
    if n == 0:
        return 'x'
    elif n == 1:
        return '(x)'
    elif n == 2:
        return '((x))'
    elif n == 3:
        return '( ((x)) )'
    else:
        if n == 4:
            return '(( ((x)) ))'
        elif n == 5:
            return '( (( ((x)) )) )'
        elif n == 6:
            return '(( (( ((x)) )) ))'
        else:
            if n % 2 == 1:
                return '( ' + annoying_parens(n - 1) + ' )'
            elif n % 2 == 0:
                return '(' + annoying_parens(n - 1) + ')'

def annoying_countdown(n):
    if n == 0:
        print(n)
        return None
    else:
        print(n)
        return annoying_countdown(n - 1)