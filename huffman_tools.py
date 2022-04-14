"""
File: huffman_tools.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Short Project #9 - Huffman Codes
"""


def str_to_codes(text, mapping):
    """ Converts a given string into a binary string.

    Parameters:
        text: a string
        mapping: a dictionary; maps single characters to binary strings
    """
    binary_strings = []
    for letter in text:
        binary_strings.append(mapping.get(letter))
    binary_strings.append(mapping.get("<END>"))
    return binary_strings


def codes_to_chunks(codes):
    """ Converts a long list of binary strings of various lengths into an
    array of 8-bit strings.

    Parameters:
        codes: a list, binary strings
    """
    long_string = ''.join(codes)

    while len(long_string) % 8 != 0:
        long_string += '0'

    length = 8
    eight_bits = []
    for i in range(0, len(long_string), length):
        eight_bits.append(long_string[i:length + i])
    return eight_bits


def print_chunks_as_decimal(chunks):
    """ Converts an 8-bit binary string into a decimal.

    Parameters:
        chunks: an array of 8-bit strings
    """
    for string in chunks:
        print(int(string, 2), end=' ')


def ints_to_bits(vals):
    """ Converts each element of an array into an 8-bit string. Combines
    the converted 8-bit strings into a large singular string.

    Parameters:
        vals: a list of integers
    """
    big_string = []
    for num in vals:
        big_string.append(bin(num)[2:].zfill(8))
    return ''.join(big_string)


def bits_to_str(bits, root):
    """ Decodes a binary string using a Huffman mapping binary tree.

    Parameters:
        bits: a binary string
        root: a binary tree, referenced for Huffman map decoding
    """
    string = ''
    pointer = root
    while len(bits) > 1:
        if bits[0] == '0':
            bits = bits[1:]
            if type(pointer.left) is str:
                if pointer.left == '<END>':
                    break
                string += pointer.left
                pointer = root
            else:
                pointer = pointer.left
        elif bits[0] == '1':
            bits = bits[1:]
            if type(pointer.right) is str:
                if pointer.right == '<END>':
                    break
                string += pointer.right
                pointer = root
            else:
                pointer = pointer.right
    return string
