# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = copy = ListNode(0)
        count = 0
        while l1 or l2:
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            new = ( a + b + count) % 10
            count = ( a + b + count ) // 10
            copy.next = ListNode(new)
            copy = copy.next
        if count == 1:
            copy.next = ListNode(1)
        return dummy.next
