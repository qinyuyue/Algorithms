## Intersection of two linked list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        """
        Algorithm - Hashtable
        1. two pointers start from two linked list separately.
        2. iterate pointer one step, either one of the pointer reaches end, connect it to the head to the other linked list.
        3. pa will meet in two condition:
            1) the start of the intersection
            2) end (None)
        """

        if not headA or not headB:
            return None
        pa = headA
        pb = headB

        while pa != pb:
            pa = headB if pa == None else pa.next
            pb = headA if pb == None else pb.next

        return pa 
