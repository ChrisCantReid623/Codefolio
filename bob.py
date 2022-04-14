"""
File: bob.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: This program processes all individual words from a text file,
        combining words in different sequences to generate palindromes of
        various lengths.
"""


def main():
    try:
        file_name = input()
        file = open(file_name, 'r')
        word_set = word_filtering(file)
        commands(word_set)
    except FileNotFoundError:
        print('ERROR: Could not open the input file: BAD_FILENAME')


def word_filtering(file):
    """ Extracts individual words from an input file into a set.

    Parameters:
        file: references the input file
    """
    word_set = set()

    for line in file:
        for word in line.split():
            word = ''.join(i for i in word if i.isalpha())
            if len(word) >= 2:
                word_set.add(word.casefold())
    return word_set


def commands(word_set):
    """ Performs different data processing based on user input. Either
    displays all words in the given set of words or proceeds to search for
    palindrome combinations.

    Parameters:
        word_set: all words from a txt file in a set

    """
    command = input()

    if command == 'dump':
        print('WORD LIST:')
        for word in sorted(word_set):
            print(f'  {word}')
    elif command.isnumeric():
        num = int(command)
        simple_palindrome(word_set)
        two_three_words(word_set)
        many_palindromes(word_set, num)


def simple_palindrome(word_set):
    """ Prints any single-word palindromes from a set of given words.

    Parameters:
        word_set: all words from a txt file in a set
    """
    print('1-WORD PALINDROMES:')
    for word in sorted(word_set):
        if word == word[::-1]:
            print(f'  {word}')
    print()


def two_three_words(word_set):
    """ Forms two and three word string combinations from the given set of
    words, printing out all palindromes.

    Parameters:
        word_set: all words from a txt file in a set
    """
    print('2-WORD AND 3-WORD PALINDROMES:')
    palindromes = set()

    #  Two Word Combinations
    for first in word_set:
        for second in word_set:
            two_words = (first + second)
            if two_words == two_words[::-1]:
                palindromes.add(two_words)

    #  Three Word Combinations
    for first in word_set:
        for second in word_set:
            for third in word_set:
                three_words = first + second + third
                if three_words == three_words[::-1]:
                    palindromes.add(three_words)

    for word in sorted(palindromes):
        print(f'  {word}')
    print()


def many_palindromes(word_set, num):
    """ Generates additional palindromes by continually combining words from
    the word set until the sequences reach a certain length.

    Parameters:
        word_set: all words from a txt file in a set
        num: an integer, the upper limit to the length of a combined sequence
        of phrases
    """
    #  Creates Dictionary Keys == Lengths, Values == Words of that Length
    lengths = dict()
    for i in range(1, num + 1):
        lengths[i] = set()

    for word in word_set:  # Adds word_set words to dictionary
        if len(word) in lengths:
            lengths[len(word)].add(word)

    for i in range(1, num + 1):  # Iterates word lengths
        print(f'PALINDROMES OF LENGTH {i}    - length of candidate list: '
              f'{len(lengths.get(i))}')

        for val in sorted(lengths.get(i)):  # Iterate through values of a certain length
            if val == val[::-1]:
                print(f'  {val}')  # PRINT PALINDROMES

            else:
                for word in word_set:
                    if word != word[::-1]:
                        combined = val + word  # Concats Non_Palindrome words from Wordset with dict value

                        if len(combined) in lengths.keys():  # Adds Newly combined word into Dictonary
                            lengths[len(combined)].add(combined)
        print()


main()
