"""
File: linked_list_recursion_long.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Long Project 5, Annoying Recursion
"""

import list_node

def array_to_list_recursive(data):
    """
    Turns a given list structure into a linked list via recursion.

    Parameters:
        data: a list/array
    """
    if len(data) == 0:
        return None
    else:
        head = list_node.ListNode(data[0])
        head.next = array_to_list_recursive(data[1:])
        return head

def accordion_recursive(old_head):
    """
    Scans a linked list, removing every other node recursively.

    Parameters:
        old_head: head pointer to a linked list
    """
    if old_head is None or old_head.next is None:
        return None
    else:
        new_head = old_head.next
        if new_head.next is not None:
            delete = old_head.next.next
            new_head.next = delete.next
            accordion_recursive(delete)
    return new_head

def pair_recursive(head1, head2):
    """ Recursively iterates two linked lists, creating tuples of each
    iterated pair. The new linked list will share the length of the shorter
    linked lists.

    Parameters:
        head1: the first linked list
        head2: the second linked list
        """
    if head1 is None or head2 is None:
        return None
    else:
        new_head = None
        combined = (head1.val, head2.val)
        combined_node = list_node.ListNode(combined)
        new_head = combined_node
        combined_node.next = pair_recursive(head1.next, head2.next)
    return new_head