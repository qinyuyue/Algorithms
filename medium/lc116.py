## Populating Next Right Pointers in Each Node

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        recursion
        1. if root.right and root.left, connect the two nodes
        2. if root.left.right and root.right.left, connect the two nodes
        """
        if root == None:
            return root
        else:
            if root.right and root.left:
                root.left.next = root.right
                if root.next and root.left:
                    root.right.next = root.next.left
                self.connect(root.left)
                self.connect(root.right)
        return root
