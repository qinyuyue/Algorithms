# Diagonal Traverse 
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Algorithm:
        start from (0,0)
        m, n is the shape of matrix
        if x + y is even, move one step to the right or upper right
        if x + y is odd, move one step to bottom or bottom left
        """

        output = []
        if matrix:
            m = len(matrix) -1
            n = len(matrix[0]) -1
            i = j = 0
            # print("m, n: ", m, n)
            while i <= m and j <= n:
                # print("i,j: ", i,j)
                # print(matrix[i][j])
                output.append(matrix[i][j])
                if (i + j) % 2 == 0:
                    if i == 0 and j != n:
                        j += 1
                    elif j == n:
                        i += 1
                    else:
                        i -= 1
                        j += 1
                elif (i + j) % 2 == 1:
                    if j == 0 and i != m:
                        i += 1
                    elif i == m:
                        j += 1
                    else:
                        i += 1
                        j -= 1
        return output
