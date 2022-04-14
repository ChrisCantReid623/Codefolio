# Author: Christopher Reid
# Course: CSC 110
# Description: This program reads in a text file and produces a information graphic based on the
#               text. The program displays the number of unique words and bar charts displaying
#               proportions of small, medium and large words and also capitalized and
#               non-capitalized words.

from graphics import graphics

def read_file(file_name):
    """
    This function reads in the contents of a text file. The name of the text file is given via
    user prompt passed in from main(). Each individual word processed by the function is appended
    to a new list.

    ---Parameters---
    file_name: the name of the file to be processed, passed in from user prompt in main()
    """
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    word_list = []
    for element in lines:
        line = element.strip('\n').split()
        for word in line:
            word_list.append(word)
    return word_list

def count_words(word_list):
    """
    This function counts the frequency of each unique word found in the list of words using a
    dictionary structure. In the key:value pairs, the keys are each unique word and the values are
    that specific word's frequency of appearance in the text file expressed as an integer.

    ---Parameters---
    word_list: a list of individual words extracted from a text file
    """
    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def count_by_category(word_count_dict):
    """
    This function measures the length of each word stored as a key in the dictionary parameter,
    categorizes the word based on length (small, medium and large) and totals the words in each
    category.

    ---Parameters---
    word_count_dict: a dictionary containing unique words and their frequencies as key:value pairs
    """
    category_counter_dict = {'small': 0, 'medium': 0, 'large': 0}
    for key, value in word_count_dict.items():
        if len(key) <= 4:
            category_counter_dict['small'] += value
        elif len(key) <= 7:
            category_counter_dict['medium'] += value
        elif len(key) >= 8:
            category_counter_dict['large'] += value
    return category_counter_dict

def most_occurring_by_size(word_count_dict):
    """
    This function measures the keys of a dictionary to determine which category it belongs (small,
    medium, large). The corresponding value is that words frequency of appearance in the txt file.
    The most frequently occurring word with the corresponding value of each category are assigned
    as a tuple in the most_occurring dictionary by category.

    Each tuple is iterated and used to concatenate to form a string that is passed back to main()
    for graphic display.

    ---Parameters---
    word_count_dict: a dictionary containing unique words and their frequencies as key:value pairs
    """
    most_occurring = {'small': ('most occurring small', 0), 'medium': ('most occurring medium', 0),
                      'large': ('most occurring large', 0)}
    for key, value in word_count_dict.items():
        if len(key) <= 4:
            if most_occurring['small'][1] < value:
                most_occurring['small'] = key, value
        elif len(key) <= 7:
            if most_occurring['medium'][1] < value:
                most_occurring['medium'] = key, value
        elif len(key) >= 8:
            if most_occurring['large'][1] < value:
                most_occurring['large'] = key, value

    string = ''
    for value in most_occurring.values():
        word, count = value
        string += word + ' (' + str(count) + 'x) '
    return string

def count_capitalized(word_count_dict):
    """
    This function processes the keys of the dictionary parameter, tracking how many words are
    capitalized and non-capitalized by the status of the first string character at index zero.

    ---Parameters---
    word_count_dict: a dictionary containing unique words and their frequencies as key:value pairs
    """
    capitalized_count = {'capitalized': 0, 'non-capitalized': 0}

    for key, value in word_count_dict.items():
        if key[0].isupper():
            capitalized_count['capitalized'] += value
        else:
            capitalized_count['non-capitalized'] += value
    return capitalized_count

def display_word_length_bar_graph(gui, word_list, category_count_dict):
    """
    This function displays the bar chart representing the proportion of unique small, medium, and
    large words.

    ---Parameters---
    gui: a graphic user interface object, the 'canvas'
    word_list: a list of individual words extracted from a text file
    category_count_dict: a dictionary tracking the total words in each category of small, medium,
    and large
    """
    unique_words = 500 / len(word_list)

    start_x = 140
    start_y = 150
    offset = 1

    # Header
    gui.text(start_x, 110, 'Word Lengths', 'white', 20)

    sml_rec_height = unique_words * category_count_dict['small']
    med_rec_height = unique_words * category_count_dict['medium']
    lrg_rec_height = unique_words * category_count_dict['large']

    med_words_start = start_y + sml_rec_height
    lrg_words_start = med_words_start + med_rec_height

    # Bar Chart
    gui.rectangle(start_x, start_y, 150, sml_rec_height, 'blue')
    gui.rectangle(start_x, med_words_start, 150, med_rec_height, 'green')
    gui.rectangle(start_x, lrg_words_start, 150, lrg_rec_height, 'blue')
    if sml_rec_height > 0:
        gui.text(start_x + offset, start_y + offset, 'Small Words', 'white', 10)
    if med_rec_height > 0:
        gui.text(start_x + offset, med_words_start + offset, 'Medium Words', 'white', 10)
    if lrg_rec_height > 0:
        gui.text(start_x + offset, lrg_words_start + offset, 'Large Words', 'white', 10)

def display_capitalized_bar_graph(gui, word_list, capitalized_count_dict):
    """
    This function displays the bar chart representing the proportion of capitalized and
    non-capitalized words.

    ---Parameters---
    gui: a graphic user interface object, the 'canvas'
    word_list: a list of individual words extracted from a text file
    capitalized_count_dict: a dictionary tracking the total words in each category of capitalized
    and non-capitalized
    """
    unique_words = 500 / len(word_list)

    start_x = 425
    start_y = 150
    offset = 1

    # Header
    gui.text(start_x, 110, 'Cap/Non-Cap', 'white', 20)

    cap_height = unique_words * capitalized_count_dict['capitalized']
    non_cap_height = unique_words * capitalized_count_dict['non-capitalized']

    cap_end = start_y + cap_height

    # Header
    gui.text(start_x, 110, 'Cap/Non-Cap', 'white', 20)

    # Bar Chart
    gui.rectangle(start_x, start_y, 150, cap_height, 'blue')
    gui.rectangle(start_x, cap_end, 150, non_cap_height, 'green')
    if cap_height > 0:
        gui.text(start_x + offset, start_y + offset, 'Capitalized Words', 'white', 10)
    if non_cap_height > 0:
        gui.text(start_x + offset, cap_end + offset, 'Non-Capitalized Words', 'white', 10)

def display_graphic_heading(gui, file_name, word_count_dict, most_occurring):
    """
    This function displays the heading context of the graphic component. The name of the file
    as given by the user, the number of unique words from the file, and the most frequently
    occurring word of each category (small, medium, and large) are displayed.

    ---Parameters---
    gui: a graphic user interface object, the 'canvas'
    file_name: the name of the txt file providing the data
    word_count_dict: a dictionary containing unique words and their frequencies as key:value pairs
    most_occurring: a string displaying most frequently occurring word of each category (small,
    medium, and large)
    """
    gui.text(5, 25, file_name, 'cyan', 20)
    gui.text(5, 50, 'Total Unique Words: ' + str(len(word_count_dict)), 'white', 20)
    gui.text(5, 75, 'Most Used Words(S/M/L):', 'white', 20)
    gui.text(250, 75, most_occurring, 'cyan', 20)

def main():
    file_name = input('Enter the name of txt file:\n')  # User Prompt

    # Data Structures
    word_list = read_file(file_name)
    word_count_dict = count_words(word_list)
    category_count_dict = count_by_category(word_count_dict)
    most_occurring = most_occurring_by_size(word_count_dict)
    capitalized_count_dict = count_capitalized(word_count_dict)

    # Graphics
    gui = graphics(650, 700, 'Infographics')
    gui.rectangle(0, 0, 650, 700, 'grey45')
    display_graphic_heading(gui, file_name, word_count_dict, most_occurring)
    display_word_length_bar_graph(gui, word_list, category_count_dict)
    display_capitalized_bar_graph(gui, word_list, capitalized_count_dict)
    gui.primary.mainloop()

main()