# Author: Christopher Reid
# Course: CSC 110
# Description: This program prompts the user for a .txt file with the purpose of rearranging each
#               new line of the file in a new order and writing that new sequence to a new .txt
#               file. An adjacent index_list, tracking the corresponding 'index' of each newline
#               location is written to a new file to be used as a 'key' in the decryption process.

import random

def randomizer(lines, index_list):
    """
    This function accepts two parameters: two list arguments passed in from main().

    The first is a list of strings read from a text file. Each element of the list represents a new
    line of the original txt file to be encrypted (order will be scrambled randomly).

    The second is a list of integers, each integer corresponds to the index of the matching line of
    the imported txt file.

    This function rearranges the lines of the text file based on indexes generated from the random
    module. The index_list acts as a 'key' to decrypt the rearrangement in an adjacent program.
    """
    for i in range(len(lines)):
        num_2 = random.randint(0, (len(lines) - 1))
        num_1 = random.randint(0, (len(lines) - 1))

        # Scrambles elements of lines
        num_holder = lines[num_2]
        lines[num_2] = lines[num_1]
        lines[num_1] = num_holder

        # Scrambles elements of index_list
        num_holder_2 = index_list[num_2]
        index_list[num_2] = index_list[num_1]
        index_list[num_1] = num_holder_2

def output_file(file_name, lst):
    """
    This function accepts two parameters: a name for a new file, and a list that provides the
    source of the new text file contents.

    The loop iterates through each element of the list, casts it as a string, and writes that
    content to the new text file.
    """
    file = open(file_name, 'w')
    for line in lst:
        file.write(str(line) + '\n')
    file.close()


def main():
    random.seed(125)

    file_name = input('Enter a name of a text file to encrypt:\n')
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    # List of numbers with the index at that same element. The length is based on how many lines
    # are in the txt file.
    index_list = []
    for i in range(len(lines)):
        index_list.append(i + 1)
        lines[i] = lines[i].strip('\n')

    for i in range(5):
        randomizer(lines, index_list)

    output_file('encrypted.txt', lines)
    output_file('index.txt', index_list)

main()