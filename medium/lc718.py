## Maximum Length of Repeated Subarray
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        Algorithm:
        1. Init a 2d matrix M, size is len(A) * len(B), full of 0.
        2. Iterate A
            iterate B
                if A[i] == B[j], M[i][j] = M[i+1][j+1] + 1
        3. Go through this matrix, get the max(max(row)), get the index, and return A[idx:idx+max].
        """

        m = len(A)
        n = len(B)
        # M = [[0] * (m+1)] * (n+1)
        M = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # print(i,j)
                if A[i] == B[j]:
                    M[i][j] = M[i+1][j+1] +1
        # print(M)
        return max(max(i) for i in M)
