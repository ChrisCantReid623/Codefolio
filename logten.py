"""
File: REPLACE_ME
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: REPLACE_ME
"""

import math

def log10(val):
    orig_val = val
    count = 0
    while val > 1:
        val = math.ceil(val / 10)
        count += 1
    return count

print(log10(1))
print(log10(10))
print(log10(100))
print(log10(1000))