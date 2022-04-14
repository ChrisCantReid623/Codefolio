"""
File: rhymes.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Given a word to compare, this program identifies additional words that
rhyme according to phonemes.
"""


def main():
    file_name = input()
    rhymes = create_dictionaries(file_name)
    while True:
        try:
            line = input()
            words_in_line = line.strip().split()
            if line == '':
                print('No word given')
                print()
            elif len(words_in_line) > 1:
                print('Multiple words entered, '
                      'please enter only one word at a time.')
                print()
            else:
                word = line.strip().upper()
                rhyme_search(word, rhymes)
        except EOFError:
            break


def create_dictionaries(dictionary_title):
    """ Converts a txt file into two dictionaries.

    Parameters:
        dictionary_title: the title of a txt file

    Returns:
        reg_dictionary: maps words to phonemes in a list
    """
    file = open(dictionary_title, 'r')

    reg_dictionary = {}

    for line in file:
        line = line.split()
        key = line[0]
        phonemes_lst = line[1:]
        if key in reg_dictionary:
            key = key.casefold()
        reg_dictionary[key] = phonemes_lst
    file.close()

    return reg_dictionary


def rhyme_search(word, w_dict):
    """ Performs the rhyme search given a word a dictionary that maps
    comparable words with their phonemes.

    Parameters:
        word: the subject word
        w_dict: the dictionary
    """
    print(f'Rhymes for: {word}')
    words_that_rhyme = []
    stress_01 = None

    #  Handles case where the Primary Stress is the first Phoneme
    phonemes = w_dict.get(word)
    if phonemes is None:
        print('-- none found --')
    else:
        for item in phonemes:
            if item[-1] == '1':
                stress_01 = item
                if phonemes.index(stress_01) == 0:
                    print('-- none found --')
                    print()
                    return
        #  Compares the stressed phoneme to words in the dictionary.
        for key, val in w_dict.items():
            if stress_01 in val:
                if val[val.index(stress_01)::] == \
                        phonemes[phonemes.index(stress_01)::]:
                    compd_prior = val[val.index(stress_01) - 1]
                    compd_final = val[-1]
                    stress_prior = phonemes[phonemes.index(stress_01) - 1]
                    phoneme_final = phonemes[-1]
                    if stress_prior != compd_prior and compd_prior is not \
                            compd_final and stress_prior is not phoneme_final:
                        if key.upper() not in words_that_rhyme:
                            words_that_rhyme.append(key.upper())
        #  Handles duplicate words identified as rhymes
        if len(words_that_rhyme) < 1:
            print('-- none found --')
        else:
            no_duplicates = []
            for word in words_that_rhyme:
                if word not in no_duplicates:
                    no_duplicates.append(word)
            for word in sorted(no_duplicates):
                print(word)
    print()


main()