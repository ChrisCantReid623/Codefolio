#! /usr/bin/python3

"""Generates a snippet of code, which represents a randomly-generated binary
   tree.  Note that this is *NOT* a BST; the arrangement of nodes is random.
   However, the values in the tree are unique.

   This will never generate a tree that is empty; if you want to test that,
   write a testcase by hand.  Likewise, it will generate very small trees (1-3
   nodes) only in *exceptional* circumstances.  It's possible, but highly
   unlikely.

   Copy the output of this program into your own program, and then use 'root'
   as the root of the tree that has been generated.
"""

import random

from tree_node import TreeNode



# generate a random set of values, which we will use to populate our tree.  It
# needs to be random, but also have unique values.  So we'll generate a random
# set (which might include duplicates), and then turn it into a set(), which
# removes duplicates, and then shuffle them.
vals_count = random.randint(5,32)
vals = [ random.randint(-50,100) for i in range(vals_count) ]
vals = set(vals)
vals = list(vals)
random.shuffle(vals)



# build the nodes.  We're doing this exactly like building a BST, except that
# it's randomly choosing whether to go left or right.

def random_insert(root, val):
    if root is None:
        return TreeNode(val)
    if random.randint(0,1) == 0:
        root.left  = random_insert(root.left,  val)
    else:
        root.right = random_insert(root.right, val)
    return root

root = None
for v in vals:
    root = random_insert(root, v)



# just in case the user doesn't realize it, this import is important.  But
# canny users won't need it...
print("from tree_node import TreeNode")
print()



# now, just print out the nodes that we've created.  To make it pretty, we'll
# use a recursive function here, which uses .left.right chains to name the
# nodes.
def print_out_subtree(root, prefix):
    print(f"{prefix} = TreeNode({root.val})")

    if root. left is not None:
        print_out_subtree(root.left, prefix+".left")
    if root.right is not None:
        print_out_subtree(root.right, prefix+".right")

print_out_subtree(root, "root")
print()


