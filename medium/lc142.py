## Linked list cycle II

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        """
        Algorithm - Hashtable
        1. store each visited to a hashtable
        2. if next node is in hashtable return head
            else, return None
        """
        visited = set()
        count = 0
        while head:
            # print(visited)
            if head.next in visited:
                return head.next
            visited.add(head)
            head = head.next
            count += 1
        return None

        """
        Algorithms - Two Pointer
        1. fast takes 2 steps while slow takes 1 step, until they meet in cycle point x.
        2. another pointer start from head takes 1 step, as well as slow. It is the begin of cycle when they meet.

        * prove of step 2:
            in this linked list, the length of acyclic part is F. It is a from start of cycle to x, while the left cycle is             b. Beacuse 2 * (F + a) = F + a + b + a, so F = b.

        """
        fast = slow = head
        cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycle = True
                break
        if cycle == False:
            return None

        while head != slow:
            head = head.next
            slow = slow.next
        return head
