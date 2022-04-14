"""Tree Algorithms"""

import tree_node
import random


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def tree_count(root):
    """
    Counts the number of nodes in binary tree.

    Parameters:
        root: references a binary tree
    """
    if root is None:
        return 0
    else:
        counter = 1
        if root.left is not None:
            counter += tree_count(root.left)
        if root.right is not None:
            counter += tree_count(root.right)
    return counter


def tree_sum(root):
    """
    Sums the values of each node in a binary tree.

    Parameters:
        root: references a binary tree
    """
    if root is None:
        return 0
    else:
        counter = root.val
        if root.left is not None:
            counter += tree_sum(root.left)
        if root.right is not None:
            counter += tree_sum(root.right)
    return counter


def tree_depth(root):
    """
    Recurs left and right subtrees, returning the levels of depth.

    Parameters:
        root: references a binary tree
    """
    if root is None:
        return -1
    return 1 + max(tree_depth(root.left), tree_depth(root.right))


def tree_print(root):
    """
    Prints the value stored in every node, one per line.

    Parameters:
        root: references a binary tree
    """
    if root is None:
        return 0
    else:
        print(root.val)
        if root.left is not None:
            tree_print(root.left)
        if root.right is not None:
            tree_print(root.right)


def tree_build_left_linked_list(data):
    """
    Builds a binary tree from an array. With each node, only the left link is
    used to outwardly build. All right links point to 'None'.

    Parameters:
        data: references an array of any length
    """
    if len(data) == 0:
        return None
    else:
        cur = root = tree_node.TreeNode(data[0])
        for item in data:
            if item != data[0]:
                cur.left = tree_node.TreeNode(item)
                cur = cur.left
        return root


def tree_height(root):
    """ Measures the height of a binary tree.

    Parameters:
        root: a binary tree
    """
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is not None and root.right is None:
        return 1 + tree_height(root.left)
    if root.left is None and root.right is not None:
        return 1 + tree_height(root.right)
    if root.left is not None and root.right is not None:
        return 1 + max(tree_height(root.left), tree_height(root.right))


def pretty_print_tree(root, indent=""):
    """ Pre-Order Traversal."""
    if root is None:
        return
    print(f'{indent}{root.val}', tree_height(root))
    pretty_print_tree(root.left, indent + ' ')
    pretty_print_tree(root.right, indent + ' ')


def pretty_print_tree2(root, indent=""):
    """ In Order Traversal. """
    if root is None:
        return
    pretty_print_tree2(root.left, indent + ' ')
    print(f'{indent}{root.val}')
    pretty_print_tree2(root.right, indent + ' ')


def random_insert(root):
    """ Generates a random number. Creates a tree nod for that value and
    inserts into a binary tree.

    Parameters:
        root: a binary tree
    """
    if root is None:
        return tree_node.TreeNode(random.randint(-100, 100))
    if random.randint(0, 1) == 0:
        root.left = random_insert(root.left)
    else:
        root.right = random_insert(root.right)
    return root


def build_random(n):
    """ Works adjacent to random_insert() function. Creates a binary tree with
    n-number of nodes.

    Parameters:
        n: an integer > 0
    """
    root = None
    for _ in range(n):
        root = random_insert(root)
    return root


def bst_insert(root, value):
    """ Inserts a given value into the correct location within a binary tree.

    Parameters:
        root: a binary tree
        value: the value to be inserted
    """
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = bst_insert(root.left, value)
    if value > root.val:
        root.right = bst_insert(root.right, value)
    return root


def bst_insert_2(root, value):
    """ Inserts a given value into the correct location within a binary tree.

    Parameters:
        root: a binary tree
        value: the value to be inserted
    """
    assert root is not None

    if value < root.val:
        if root.left is None:
            root.left = TreeNode(value)
        else:
            bst_insert_2(root.left, value)
    else:
        if root.right is None:
            root.right = TreeNode(value)
        else:
            bst_insert_2(root.right, value)


def bst_builder(array):
    """ Builds a binary tree from an array of numbers.

    Parameters:
        array: a list of numbers
    """
    root = tree_node.TreeNode(array[0])
    i = 1
    for i in range(len(array[::1])):
        bst_insert(root, array[i])
    return root


def bad_bst(array):
    """ Basically creates a linked list from an array of integers. Uses a tree
    node instead of a list node.

    Parameters:
        array: a list of numbers
    """
    if not array:
        return None
    node = tree_node.TreeNode(array[0])
    node.right = bad_bst(array[1:])
    return node


def bst_builder2(array):
    """ Builds a binary tree from an array of numbers.

       Parameters:
           array: a list of numbers
    """
    if not array:
        return None
    middle = len(array)//2
    node = tree_node.TreeNode(array[middle])
    node.left = bst_builder2(array[:middle])
    node.right = bst_builder2(array[middle + 1:])
    return node


def random_thirty():
    """ Creates a list of 30 randomly generated numbers. """
    thirty = []
    for i in range(30):
        thirty.append(random.randint(1, 100))
    return thirty


def array_to_perf_bst(data):
    """ Converts an array of numbers into a binary search tree.

    Parameters:
        data: a list of numbers
    """
    if len(data) == 0:
        return None
    data_sorted = sorted(data)
    mid = len(data_sorted)//2
    mid_val = data_sorted[mid]

    left = data_sorted[:mid]
    right = data_sorted[mid + 1:]

    retval = tree_node.TreeNode(mid_val)
    retval.left = array_to_perf_bst(left)
    retval.right = array_to_perf_bst(right)
    return retval


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


# ------ Sample Trees --------
tree1 = tree_node.TreeNode(74)
tree1.left = tree_node.TreeNode(4)
tree1.right = tree_node.TreeNode(80)
tree1.left .left = tree_node.TreeNode(0)
tree1.left .right = tree_node.TreeNode(17)
tree1.right.left = tree_node.TreeNode(77)
tree1.right.right = tree_node.TreeNode(96)

tree2 = tree_node.TreeNode(69)
tree2.left = tree_node.TreeNode(38)
tree2.right = tree_node.TreeNode(63)
tree2.left .left = tree_node.TreeNode(53)
tree2.left .right = tree_node.TreeNode(68)
tree2.right.left = tree_node.TreeNode(88)
tree2.right.right = tree_node.TreeNode(46)

# ------- Test Code ---------
numbers = random_thirty()  # Random 30 numbers

pretty_print_tree(tree1)  # Tree # 1
pretty_print_tree(tree2)  # Tree # 2

pretty_print_tree(build_random(4))

pretty_print_tree(bst_builder2(sorted(numbers)))
pretty_print_tree(bad_bst(sorted(numbers)))

