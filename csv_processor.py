# Author: Christopher Reid
# Course: CSC 110
# Description: This program reads in a CSV file reading in each row as a line in a two dimensional
#               list. The user is then prompted for a common column, using the values at that column
#               of each row as data. Using that new data set, the user is promoted to compute
#               the maximum value, minimum value, or the average.

def calculate_minimum(two_d_list, column):
    """
    This function first iterates through each row of numbers, then through each number keeping
    track of each number's index. In each row at , the numbers at the [count index]
    (column parameter minus 1) are added to an new empty list. The new list is then sorted in
    ascending order where the element at index zero will always contain the minimum value.

    two_d_list: self explanatory, a 2 dimensional list created in main()
    column: an integer passed in from main()
    """
    values = []
    count_index = column - 1
    for row in two_d_list:
        for num in row:
            if row.index(num) == count_index:
                values.append(num)

    # Sorts by ascending values
    values.sort()
    # Find the minimum value
    minimum = values[0]
    return minimum

def calculate_maximum(two_d_list, column):
    """
    This function first iterates through each row of numbers, then through each number keeping
    track of each number's index. In each row,the numbers at the [count index]
    (column parameter minus 1) are added to an new empty list and converted to floats. Each value
    of the new list is iterated, checking for the maximum value and assigning the 'maximum'
    variable.

    two_d_list: self explanatory, a 2 dimensional list created in main()
    column: an integer passed in from main()
    """
    values = []
    count_index = column - 1
    for row in two_d_list:
        index = 0
        for num in row:
            if index == count_index:
                values.append(num)
            index += 1

    # Find the maximum value
    maximum = 0
    for item in values:
        item = float(item)
        if item > maximum:
            maximum = item
    return maximum

def calculate_average(two_d_list, column):
    """
    This function first iterates through each row of numbers, then through each number keeping
    track of each number's index. In each row,the numbers at the [count index]
    (column parameter minus 1) are added to an new empty list and converted to floats. Each value
    of the new list is iterated, converted to a float and accumulated onto the sum variable. The
    sum variable is then used to calculate the average of the new list.

    two_d_list: self explanatory, a 2 dimensional list created in main()
    column: an integer passed in from main()
    """
    sum_list = []
    count_index = column - 1
    for row in two_d_list:
        index = 0
        for num in row:
            if index == count_index:
                sum_list.append(num)
            index += 1

    # Accumulate sum and calculate average
    sum = 0
    for item in sum_list:
        sum += float(item)
    average = sum / len(two_d_list)
    return average

def main():
    # User Prompts
    file_name = input('Enter CSV file name:\n')
    col_num = int(input('Enter column number:\n'))
    col_op = input('Enter column operation:\n')

    # Creates 2D list of a csv file
    file = open(file_name, 'r')
    # file = open('more_numbers.csv', 'r')
    two_dimen_lst = []
    for line in file:
        line = line.strip('\n').split(',')
        two_dimen_lst.append(line)
    file.close()

    # Passing the 2D list and column number as arguments
    if col_op == 'min':
        result = calculate_minimum(two_dimen_lst, col_num)
        print('The minimum value in column', col_num, 'is:', float(result))
    elif col_op == 'max':
        result = calculate_maximum(two_dimen_lst, col_num)
        print('The maximum value in column', col_num, 'is:', float(result))
    elif col_op == 'avg':
        result = calculate_average(two_dimen_lst, col_num)
        print('The average for column', col_num, 'is:', float(result))

main()