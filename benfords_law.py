# Author: Christopher Reid
# Course: CSC 110
# Description: The program extracts the number values from a .csv file, calculating the
#               proportional distribution of numbers beginning with each digit, 1 through 9. The
#               proportions are visually displayed in a hashtag bar graph and the percentages are
#               analyzed to determine if the numbers from the data follow Benford's Law.

def create_lines_list(file):
    """
    This function reads each line of a .csv file, converting each number to a floating
    point number and appending it to an empty list.

    ---Parameters---
    file: a .csv file determined by a user prompt in main()
    """
    num_lst = []
    lines = file.readlines()
    for line in lines:
        line = line.strip('\n').split(',')
        for element in line:
            if element[0].isnumeric() and int(element[0]) != 0 and element[-1].isnumeric():
                num_lst.append(float(element))
    return num_lst

def create_plot(num_lst):
    """
    This function iterates through a list of floating point values reading the first character. A
    new dictionary counts how many times a number begins with a specific digit.

    ---Parameters---
    num_list: a list of floating point values taken from a .csv file
    """
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    start = 1
    end = 10
    for number in num_lst:
        for x in range(start, end, 1):
            if int(str(number)[0]) == x:
                counts[x] += 1
    return counts

def number_percentages(count_dict, num_lst):
    """
    This function calculates the percentage of numbers beginning with a specific digit occurring in
    a .csv file.

    ---Parameters---
    count_dict: a dictionary counting how many times a number begins with a specific digit
    num_list: a list of floating point values taken from a .csv file
    """
    percentages = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for key, value in count_dict.items():
        percent = ((value / len(num_lst)) * 100)
        percentages[key] = int(percent)
    return percentages

def bar_chart(percentages):
    """
    This function prints a visual representation of the percentage data, printing as many
    hashtags as that specific number's proportional occurrence from the .csv file.

    ---Parameters---
    percentages: a dictionary with percentage calculations of each specific digits occurrence
    within the .csv file
    """
    for key, value in percentages.items():
        print(key, '|', str('#' * value))

def determine_benfords_law(percentages):
    """
    This function determines if the digit distribution follows Benford's Law using the percentages
    dictionary. For every digit (key), the percentage (value) must fall within a certain range.

    Every digit testing 'True' for this condition adds to an accumulator variable. If the
    accumulator never reaches a value of 9 (1 for each digit), then the data set does not meet
    Benford's law. The range for each individual digit is 10% higher or 5% lower than the
    derivative base percentage.

    ---Parameters---
    percentages: a dictionary with percentage calculations of each specific digits occurrence
    within the .csv file
    """
    follow_count = 0  # Counts how many digits (1-9) fit their specific percentage parameters
    for key, value in percentages.items():
        if key == 1 and 25 <= value <= 40:  # Base Percentage: 30%
            follow_count += 1
        elif key == 2 and 12 <= value <= 27:  # Base Percentage: 17%
            follow_count += 1
        elif key == 3 and 7 <= value <= 22:  # Base Percentage: 12%
            follow_count += 1
        elif key == 4 and 4 <= value <= 19:  # Base Percentage 9%
            follow_count += 1
        elif key == 5 and 2 <= value <= 17:  # Base Percentage 7%
            follow_count += 1
        elif key == 6 and 1 <= value <= 16:  # Base Percentage 6%
            follow_count += 1
        elif key == 7 or key == 8 and value <= 15:  # Base Percentage 5%
            follow_count += 1
        elif key == 9 and value <= 14:  # Base Percentage 4%
            follow_count += 1

    if follow_count < 9:
        print('Does not follow Benford\'s Law')
    else:
        print('Follows Benford\'s Law')

def main():
    file_name = input('Data file name:\n')
    print()
    file = open(file_name, 'r')

    num_lst = create_lines_list(file)
    file.close()
    counts = create_plot(num_lst)
    percentages = number_percentages(counts, num_lst)
    bar_chart(percentages)
    print()
    determine_benfords_law(percentages)
main()