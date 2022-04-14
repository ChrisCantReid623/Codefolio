"""
    list_node.py

    Contains a simple ListNode class, which simply has 'val' and 'next' fields.
"""

class ListNode:
    """ Models a single node in a singly-linked list.  Has no methods, other
        than the constructor.
    """

    def __init__(self, val):
        """ Constructs the object; caller must pass a value, which will be
            stored in the 'val' field.
        """

        self.val = val
        self.next = None

    def __str__(self):
        vals = []
        objs = set()
        curr = self
        while curr is not None:
            curr_str = str(curr.val)
            if curr in objs:
                vals.append("{} -> ... (to infinity and beyond)".format(curr_str))
                break
            else:
                vals.append(curr_str)
                objs.add(curr)
            curr = curr.next

        return " -> ".join(vals)
