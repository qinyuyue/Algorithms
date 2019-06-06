## Odd even linked list 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        """
        Algorithms:
        notice: must use a copy to store the begining of LinkNode
        """

        dummy2 = even = ListNode(0)
        dummy1 = odd = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next ## even can be None, if even is None, then means head is on the tail now.
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next
