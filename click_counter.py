"""
File: ____________________.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: __________________
"""

class Counter:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count += 1

    def get_count(self):
        return self.count

    def reset(self):
        self.count = 0

year = Counter()
for count in range(0, 365):
    year.click()
print(year.get_count())

february = Counter()
for count in range(0, 28):
    february.click()
print(february.get_count())

leap_year = Counter()
for count in range(0, 29):
    leap_year.click()
print(leap_year.get_count())