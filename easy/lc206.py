# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        """
        Algorithm - Iterative
        1. prev, curr, head
        2. curr = head, curr.next = prev, prev = curr
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev

        """
        Algorithm - Recursive
        """
        if head == None or head.next == None:
            return head
        curr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return curr
