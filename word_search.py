# File: word_search.py
# Author: Christopher Reid
# CSC 120 Spring 2022
# Purpose: This function searches a 2D matrix structure of random characters
#           scanning for a sequential existence of one or more words in one
#           of eight possible directions.

def prep_word_search(file):
    """This function creates the 2D grid of lists from a txt file and
    identifies the word(s) being searched.

    ---Parameters---
    file: the name of the file containing the word search txt file"""

    line_lst = []
    for line in file.readlines():
        if line != '\n':
            line = line.strip('\n')
            line_lst.append(line)
        else:
            line_lst.append('Delete')

    #  Word Being Searched
    words = []
    for element in line_lst[::-1]:
        if element != "Delete":
            words.append(element)
            line_lst.remove(element)
        else:
            line_lst.remove(element)
            break

    #  Creates Word Search 2D Grid
    grid = []
    for line in line_lst:
        row = []
        for letter in line:
            row.append(letter)
        grid.append(row)

    return grid, words


def letter_search(grid, word):
    """This function checks to find the word in the matrix and prints results.

    ---Parameters---
    grid: a 2D matrix structure

    word: the word being search in the grid"""
    start_position = []
    first_char = word[0]

    for row in range(0, len(grid)):
        for column in range(0, len(grid[row])):
            if grid[row][column] == first_char:
                start_position.append([row, column])

    #  Checks every starting position for word
    for position in start_position:
        if check_start(grid, word, position):
            #  Word Found
            return

    print('Word \'' f'{word}' '\' not found')
    print()


def check_start(grid, word, starting_position):
    """This function checks if the word starts at the starting position.
    Returns True if word is found.

    ---Parameters---
    grid: a 2D matrix structure

    word: the word being search in the grid

    starting_position: the (x,y) matrix coordinate for every location where
    the first letter of the word exists"""

    directions = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1],
                  [1, -1]]

    for direction in directions:
        if check_direction(grid, word, starting_position, direction):
            return True


def check_direction(grid, word, starting_position, direction):
    """This function checks if the word is in a specific direction from the
    start position in the grid. Returns True if word is found.

    ---Parameters---
    grid: a 2D matrix structure

    word: the word being search in the grid

    starting_position: the (x,y) matrix coordinate for every location where
    the first letter of the word exists

    direction: each element contains a integer pair that modifies the (x,y)
    matrix location being scanned"""

    found_characters = [word[0]]  # Characters found in direction.
    current = starting_position  # Position being searched for
    position = [starting_position]  # Positions already searched

    while characters_match(found_characters, word):
        if len(found_characters) == len(word):
            #  If found all characters and all characters found are correct,
            #  words has been found.
            for x in range(0, len(grid)):
                line = ""
                for y in range(0, len(grid[x])):
                    is_position = False
                    for z in position:
                        if (z[0] == x) and (z[1] == y):
                            is_position = True
                    if is_position:
                        line = line + grid[x][y]
                    else:
                        line = line + '.'
                print(line)
            print()
            return True
        current = [current[0] + direction[0], current[1] + direction[1]]
        position.append(current)
        if valid_index(grid, current[0], current[1]):
            found_characters.append(grid[current[0]][current[1]])
        else:
            return


def characters_match(found, word):
    """This function checks if the found letters match the word being
    searched for.

    ---Parameters---
    word: the word being search in the grid

    found: the characters from a starting letter's particular point
    identified as matching the word being searched"""
    index = 0
    for letter in found:
        if letter != word[index]:
            return False
        index += 1
    return True


def valid_index(grid, row, column):
    """This function checks if the provided line row and column numbers are
    valid so the
    scan can remain inside the grid limits.

    ---Parameters---
    grid: a 2D matrix structure

    row: a single element of the grid, contains a list of characters

    column: used to iterate each element of a row, scans each individual for
    comparisons"""
    if (row >= 0) and (row < len(grid)):
        if (column >= 0) and (column < len(grid[row])):
            return True
    return False


def main():
    file_name = input('Please give the puzzle filename:\n')
    file = open(file_name, 'r')
    grid, words = prep_word_search(file)
    for word in words[::-1]:
        letter_search(grid, word)

main()