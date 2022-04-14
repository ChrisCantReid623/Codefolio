"""
File: linked_list_short.py.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Short Project #5
"""

import list_node

def list_to_array(head):
    """
    This function converts a linked list to a list containing the same values.

    ---Parameters---
    head: a variable pointing to a linked list data structure

    ---Return Values---
    same_values: a list, contains the values of each node of the linked list
    """
    same_values = []

    if head is None:
        return same_values
    else:
        cur = head
        while cur.next is not None:
            same_values.append(cur.val)
            cur = cur.next
        same_values.append(cur.val)
        return same_values

def array_to_list(data):
    """
    This function modifies a list/array into a linked list.

    ---Parameters---
    data: a list or array

    ---Return Values---
    head: a variable, represents the linked list structure. Points to the
    first node.
    """
    if len(data) == 0:
        head = None
        return head
    else:
        cur = head = list_node.ListNode(data[0])
        for item in data:
            if item != data[0]:
                cur.next = list_node.ListNode(item)
                cur = cur.next
        return head

def list_length(head):
    """
    This function counts the number of nodes in a linked list. Using the cur
    pointer to traverse the list, everytime a new node is reached,
    the counter variable adds 1.

    ---Parameters---
    head: a variable, represents the linked list structure. Points to the
    first node

    ---Return Values---
    count: an integer, tracks the number of nodes in a linked list
    """
    count = 0
    cur = head
    while cur.next is not None:
        count += 1
        cur = cur.next
    count += 1
    return count

def is_sorted(head):
    """
    This function scans a linked list, checking if the nodes are ordered
    sequentially by their values. If one node is found to be out of order,
    the function returns False.

    ---Parameters---
    head: a variable, represents the linked list structure. Points to the
    first node
    """
    if head is None:
        return True
    else:
        cur = head
        while cur.next is not None:
            if cur.val > cur.next.val:
                return False
            cur = cur.next
        return True

def accordion(old_head):
    """
    This function traverses a linked list starting with the second node,
    only keeping every alternate node. Each node in-between has its link
    reference reassigned as to be garbage collected.

    ---Parameters---
    old_head: a linked list, points to the first node

    ---Return Values---
    new_head: a linked list, returned with only the values from the
    alternate nodes of the original linked list
    """
    if old_head is None or old_head.next is None:
        return None
    else:
        new_head = old_head.next

        prev = new_head
        now = new_head.next

        while prev is not None and now is not None:
            prev.next = now.next
            now = None
            prev = prev.next
            if prev is not None:
                now = prev.next
        return new_head