"""
File: tree_funcs_long.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Long Project #8, Trees (Long)
"""

import tree_node


def bst_search_loop(root, value):
    """ Uses a while loop to search for a given value within a BST.

    Parameters:
        root: a binary search tree
        value: the subject search value
    """
    cur = root
    while cur is not None:
        if cur.val == value:
            return cur
        if value < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    return


def tree_search(root, value):
    """ Searches a given value within a binary tree.

    Parameters:
        root: a binary tree
        value: the subject search value
    """
    if root is not None:
        if root.val == value:
            return root
        else:
            cur = tree_search(root.left, value)
            if cur is not None:
                return cur
            return tree_search(root.right, value)
    return


def bst_insert_loop(root, value):
    """ Inserts a given value into a pre-existing binary tree.

    Parameters:
        root: the pre-existing search binary tree
        value: the value being inserted
    """
    new_node = tree_node.TreeNode(value)
    x = root
    y = None
    while x is not None:
        y = x
        if value < x.val:
            x = x.left
        else:
            x = x.right
    if y is None:
        y = new_node
    elif value < y.val:
        y.left = new_node
    else:
        y.right = new_node
    return y


def pre_order_traversal_print(root):
    """ Prints values of a binary tree using a pre-order traversal.

    Parameters:
        root: a binary tree
    """
    if root:
        print(root.val)
        pre_order_traversal_print(root.left)
        pre_order_traversal_print(root.right)


def in_order_traversal_print(root):
    """ Prints values of a binary tree using an in-order traversal.

    Parameters:
        root: a binary tree
    """
    if root:
        in_order_traversal_print(root.left)
        print(root.val)
        in_order_traversal_print(root.right)


def post_order_traversal_print(root):
    """ Prints values of a binary tree using a post-order traversal.

    Parameters:
        root: a binary tree
    """
    if root:
        post_order_traversal_print(root.left)
        post_order_traversal_print(root.right)
        print(root.val)


def in_order_vals(root):
    """ Returns an array of values, gathered from an in-order traversal of a
    binary tree.

    Parameters:
        root: a binary tree
    """
    node_values = []
    if root:
        node_values = in_order_vals(root.left)
        node_values.append(root.val)
        node_values = node_values + in_order_vals(root.right)
    return node_values


def bst_max(root):
    """ Returns the maximum value of a binary search tree.

    Parameters:
        root: a binary search tree
    """
    cur = root
    while cur.right:
        cur = cur.right
    return cur.val


def tree_max(root):
    """ Returns the maximum value of a binary tree.

    Parameters:
        root: a binary tree
    """
    node_values = []
    if root:
        node_values = in_order_vals(root.left)
        node_values.append(root.val)
        node_values = node_values + in_order_vals(root.right)
    return max(node_values)
