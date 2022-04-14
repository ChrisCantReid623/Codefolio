"""
File: REPLACE_ME
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Remove Duplicates
"""

import random


'''a = random.randint(1, 12)
b = random.randint(1, 12)
for i in range(10):
    question = f"What is " + str(a) + " x " + str(b) + "? "
    answer = input(question)
    if answer == a*b:
        print('Well done!')
    else:
        print("No.")'''

def remove_dups(arr):
    i = 0
    while i < len(arr):
        j = i+1
        while j < len(arr):
            if arr[j] == arr[i]:
                arr.pop(j)
            else:
                j += 1
        i += 1
    return arr

data = [-50, 66, 80, 58, -50, 86, -19, -35, 45, 80, 80, -6, 34]

print(remove_dups(data))