# File: grid_scan.py
# Author: Christopher Reid
# Course: CSC 120 Spring 2022
# Purpose: This program reads the contents of a txt file, a grid of random
#           characters, scanning for specific string characters, determined
#           by the input from the user. Those characters will be replaced
#           with a period within the grid output. The scanned characters are
#           concatenated for form a string combining all the searched
#           characters from withing the grid.

def build_grid(original_grid):
    """
    This function creates a two-dimensional list structure. Each line is
    turned into a separate element of a list. Then each element of that line
    contains the individual characters of the line.


    ---Parameters---
        original_grid: the txt file containing the grid of characters to be
    scanned
    """
    
    starting_grid = []

    for line in original_grid:
        if len(line.strip()) != 0:
            line = line.strip()
            character_lst = []
            for character in line:
                character_lst.append(character)
            starting_grid.append(character_lst)
    return starting_grid

def reverse_grid(starting_grid):
    """
    This function simply reverses the order of the grid so that rows and
    columns can be indexed in a coordinate plane orientation, such that the
    character in the bottom left of the txt file would have an
    (x,y) coordinate location of (0,0)

    ---Parameters---
        starting_grid: a two-dimensional list structure where each line of the txt
    file makes up the first dimension and each individual character on that
    line makes up the second dimension
    """

    searching_grid = []
    for element in starting_grid[::-1]:
        searching_grid.append(element)
    return searching_grid

def character_search(search_commands, searching_grid):
    """
    This function takes the user input from the user, concatenating each
    scanned character onto a building string held within a variable. Should
    the scan overshoot the dimensions of the list, the program will stop,
    outputting an error message for the user. Each scanned character is
    replaced within the two-dimensional list with a period ('.').

    ---Parameters---
    search_commands: the user input commands with the following format:
                    Scan Direction, X-Start, Y-Start, Scan-Count

    searching_grid: a two-dimensional grid structure where each row is
    represent in the first dimension of the list and then each column is
    represented by the individual characters of the second dimension
    """

    searched_characters = ''

    search_commands = search_commands.split(' ')

    direction = search_commands[0]
    starting_x = int(search_commands[1])
    starting_y = int(search_commands[2])
    count = int(search_commands[3])

    x = starting_x
    y = starting_y

    if count > len(searching_grid):
        print(f'ERROR: Could not collect {count} letters, starting at ('
              f'{starting_x},'
              f'{starting_y}), because it fell off of the grid.')
        return

    else:
        if direction == 'N':
            for i in range(count):
                searched_characters += searching_grid[y][x]
                searching_grid[y][x] = '.'
                y += 1

        elif direction == "E":
            for i in range(count):
                if x < len(searching_grid[y]):
                    searched_characters += searching_grid[y][x]
                    searching_grid[y][x] = '.'
                    x += 1
                else:
                    print(
                        f'ERROR: Could not collect {count} letters, starting '
                        f'at ({starting_x},'
                        f'{starting_y}), because it fell off of the grid.')
                    return
        elif direction == "SW":
            for i in range(count):
                searched_characters += searching_grid[y][x]
                searching_grid[y][x] = '.'
                x -= 1
                y -= 1

        print(searched_characters)
        return searching_grid

def output_dotted_grid(dotted_grid):
    """
    If a full grid scan is completed, this function reverses the grid
    modified with periods marking scanned characters from the
    character_search() function for output orientation.

    ---Parameters---
        dotted_grid: the scanned result of the character_search function. All
        scanned characters will be marked by a period ('.') where they once
    existed
    """

    if dotted_grid:
        reversed_grid = []

        for element in dotted_grid[::-1]:
            reversed_grid.append(element)

        for row in reversed_grid:
            for character in row:
                print(character, end='')
            print('\n', end='')

def main():
    file_name = input()
    file = open(file_name, 'r')
    grid_file = file.readlines()
    file.close()

    search_commands = input()  # User Input

    #  Builds Grids
    starting_grid = build_grid(grid_file)
    searching_grid = reverse_grid(starting_grid)
    dotted_grid = character_search(search_commands, searching_grid)
    output_dotted_grid(dotted_grid)

main()