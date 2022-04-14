"""
File: linked_list_recursion_short.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Short PA # 7
"""

def is_rev_sorted(head):
    if head is None:
        return True
    else:
        cur = head
        while cur.next is not None:
            if cur.next.val <= cur.val:
                cur = cur.next
            else:
                return False
        return True

def is_rev_sorted_recursive(head):
    if head is None:
        return True
    else:
        cur = head
        while cur.next is not None:
            if cur.next.val <= cur.val:
                return is_rev_sorted_recursive(cur.next)
            else:
                return False
        return True