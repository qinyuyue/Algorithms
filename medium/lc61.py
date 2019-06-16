# Rotate List 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        Algorithms:
        1. go through and calculate the length of linked list
        2. find the node before new head, reassign its next to null
        3. concatenate the end of this list to the original head
        4. return new head
        """
        if k == 0 or not head:
            return head
        else:
            dummy1 = dummy2 = head
            count = 0
            while head.next:
                head = head.next
                count += 1
            if k%(count+1) == 0:
                return dummy1
            for i in range(count-k%(count+1)):
                dummy1 = dummy1.next
            output = dummy1.next
            dummy1.next = None
            head.next = dummy2
            return output
