## Sort array by parity

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = 0
        b = len(A) - 1
        while a < b:
            if A[a] % 2 == 0:
                a += 1
            if A[b] % 2 == 1:
                b -= 1
            else:
                A[a], A[b] = A[b], A[a]
        return A
