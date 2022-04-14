"""
File: ____________________
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: __________________
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

twenty_four = TreeNode(24)
twelve = TreeNode(12)
thirty_six = TreeNode(36)
ten = TreeNode(10)
fifteen = TreeNode(15)
twenty_five = TreeNode(25)
forty = TreeNode(40)

twenty_four.left = twelve
twenty_four.right = thirty_six
twelve.left = ten
twelve.right = fifteen
thirty_six.left = twenty_five
thirty_six.right = forty

root = twenty_four
