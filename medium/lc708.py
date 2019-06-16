# Insert into a Cyclic Sorted List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        dummy = head
        node = Node(insertVal, None)
        if head == None:
            node.next = node
            head = node
            return head
        while head:
            if head.next == dummy:
                node.next = head.next
                head.next = node
                break
            elif insertVal >= head.val and insertVal < head.next.val:
                node.next = head.next
                head.next = node
                break
            elif insertVal >= head.val and head.val > head.next.val:
                node.next = head.next
                head.next = node
                break
            elif insertVal < head.val and head.val > head.next.val and insertVal < head.next.val:
                node.next = head.next
                head.next = node
                break
            else:
                head = head.next
        return dummy
