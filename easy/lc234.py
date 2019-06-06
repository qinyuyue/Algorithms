## Palindrome Linked List 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        """
        Algorithm:
        1. Find the meddle node by fast and slow pointer
        2. reverse the rest part of slow
        3. compare orginal or head with middle of node one by one, to see if equal
        """
        fast = slow = head

        ## find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        ## reverse the rest part from middle
        prev = None

        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        while prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        return True
