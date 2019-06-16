# Flatten a Multilevel Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # dummy = node = ListNode(0)
        dummy = head
        # parent = None
        sibling_list = []
        # if head.child:
        #     sibling_list.append(head.next)
        while head:
            # print(head.val)
            if head.next == None and head.child == None:
                if sibling_list:
                    sibling = sibling_list.pop()
                    # print(sibling.val)
                    head.next = sibling
                    sibling.prev = head
                    sibling = None
                    head = head.next
                else:
                    return dummy
            elif head.child:
                if head.next != None:
                    sibling_list.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
                head = head.next

            else:
                head = head.next

        return dummy
