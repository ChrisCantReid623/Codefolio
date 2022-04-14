"""
File: unzip.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: This function returns a string. The string represents the
        decompressed data provided in a list of tokens, all of which represent
        data in a compressed string sequence.
"""


def unzip(compressed):
    uncompressed = ''
    for item in compressed:
        assert isinstance(item, (str, tuple))

        #  HANDLE STRINGS
        if isinstance(item, str):
            assert len(item) >= 1
            uncompressed += item

        #  HANDLE TUPLES
        elif isinstance(item, tuple):
            assert len(item) == 2
            assert type(item[0]) == int and item[0] > 0
            assert type(item[1]) == int and item[1] > 0
            assert item[0] <= len(uncompressed)

            add_on = uncompressed[-item[0]: -item[0] + item[1]]
            if len(add_on) >= item[1]:
                uncompressed += add_on

            #  HANDLE OVERLAPPING CHARACTER COPIES
            else:
                for count in range(1, item[1] + 1):
                    copy = uncompressed[-item[0]]
                    uncompressed += copy
    return uncompressed
