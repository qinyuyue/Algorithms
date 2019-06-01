## Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Algorithm:

        ## use boarder to restrict the value
        1. 4 variables, minr, maxr, minc, maxc
        2. while minr <= maxr and minc <== maxc:
            for minc <= i <= maxc, i++,  push matrix[minr][i]
            for minr <= i <= maxc, i++, push matrix[i][maxc]
            if minr > maxr or minc > maxc:
                for minc <= i <= maxc, i--,  push matrix[maxr][i]
                for minr <= i <= maxc, i--, push matrix[i][minc]

        ## original thought, read and change matrix to infinite
        1. m, n is the shape of matrix
        2. when position was read, change it to infinite
        3. start from (0,0), j++ until j == n
        4. if value of i+1 != infinite or i+1, j == n, i++,
        5. elif value of i+1 == infinite, j-- until j == 0 or vaule is infinite
        6. elif value of j-1 == infinite, i-- until value of i-1 is infinite

        """

        output = []
        if matrix:
            minr = minc = 0
            maxr = len(matrix) - 1
            maxc = len(matrix[0]) - 1
            # i = 0
            while minr <= maxr and minc <= maxc:
                for i in range(minc, maxc+1):
                    output.append(matrix[minr][i])
                minr += 1
                for i in range(minr, maxr+1):
                    output.append(matrix[i][maxc])
                maxc -= 1
                if minr > maxr or minc > maxc:
                    break
                for i in range(maxc, minc-1, -1):
                    output.append(matrix[maxr][i])
                maxr -= 1
                for i in range(maxr, minr-1, -1):
                    output.append(matrix[i][minc])
                minc += 1
        return output
