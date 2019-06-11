## Merge two ordered linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        """
        Algorithm - Recursive:
        """
        # if l1 == None:
        #     return l2
        # elif l2 == None:
        #     return l1
        # elif l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        """
        Algorithm - Iterative:
        """
        output = copy = ListNode(0)
        while l1 or l2:
            if not l1:
                copy.next = l2
                l2 = None
                # return output.next
                # return output.next
            elif not l2:
                copy.next = l1
                l1 = None
                # return output.next
            elif l1.val <= l2.val:
                copy.next = l1
                copy = copy.next
                l1 = l1.next
            else:
                copy.next = l2
                copy = copy.next
                l2 = l2.next
        return output.next
