# Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = node = Node(0, None, None)
        dic = {}
        while head:
            val = head.val
            if head in dic:
                curr = dic[head]
            else:
                curr = Node(val, None, None)
                dic[head] = curr
            node.next = curr
            if head.random in dic:
                curr.random = dic[head.random]
            elif head.random:
                rand = Node(head.random.val, None, None)
                dic[head.random] = rand
                curr.random = rand
            node = node.next
            head = head.next
        return dummy.next
