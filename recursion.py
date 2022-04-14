""" Recursive Functions"""
###############################################################################
def count_coins_in_cup(cup):
    """ Essentially counting the length of a list. """
    if cup == []:
        return 0
    else:
        count = 1 + count_coins_in_cup(cup[1:])
    return count


# EXECUTION
letters = ['c', 'h', 'r', 'i', 's']
nums = count_coins_in_cup(letters)
###############################################################################
def last_in_linked_list(cur):
    """ Finds the last element in a linked list. """
    if cur is None:
        return None
    if cur.next is None:
        return cur.val
    else:
        return last_in_linked_list(cur.next)

# EXECUTION
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = ListNode('First')
node2 = ListNode('Second')
node3 = ListNode('Third')

node1.next = node2
node2.next = node3

head = node1

last = last_in_linked_list(head)
###############################################################################
def count_odd_values(array):
    """ Counts odd values in list. """
    if array == []:
        return 0
    else:
        if array[0] % 2 == 1:
            count = 1 + count_odd_values(array[1:])
        else:
            count = count_odd_values(array[1:])
    return count

# EXECUTION
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odds = count_odd_values(lst)
###############################################################################
def found_in_linked_list(cur, k):
    """ Determines if a value is present in a linked list. """
    if cur is None:
        print(f'{k} is NOT in this linked list')
        return False
    if cur.val == k:
        print(f'{k} is in this linked list')
        return True
    else:
        return found_in_linked_list(cur.next, k)

# EXECUTION
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

head = node1

answer = found_in_linked_list(head, None)
###############################################################################
def how_much_money(cup):
    """ Sums up the contents of a list. """
    # Base Case
    if len(cup) == 0:
        return 0
    else:
        #  Recursion with List Slicing
        money = cup[0] + how_much_money(cup[1:])
    return money

# EXECUTION
lst = [1, 2, 3]
total = how_much_money(lst)
###############################################################################
def how_much_money_ll(cup):
    """ Sums of the contents of a linked list. """
    # Base Case
    if cup.next is None:
        return 0
    else:
        return cup.val + how_much_money_ll(cup.next)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# EXECUTION
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

head = node1

total = how_much_money_ll(head)
###############################################################################
def recursive_string_concatenation(string, integer):
    """ Self concatenates a given string by a factor of the given integer.
    Parameters:
        string: a string
        integer: a non-negative integer
    """
    if integer == 0:
        return ''
    else:
        return string + recursive_string_concatenation(string, integer-1)
