## Pascal's Triangle 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Recursive
        """
        if numRows == 0:
            return []
        # output = [[1]]
        # print(output[-1])
        def helper(num):
            if num == 1:
                output = [[1]]
            else:
                output = helper(num-1)
                pre_row = output[-1]
                cur_row = []
                for j in range(num):
                    if j == 0:
                        cur_row.append(1)
                    elif j < (num -1):
                        cur_row.append(pre_row[j-1] + pre_row[j])
                    else:
                        cur_row.append(1)
                output.append(cur_row)
            return output
        return helper(numRows)


        """
        Iterative Algorithm
        1. for each new row, start and end equal to 1, others equal to output[i-1][j] + output[i-1][j+1],
        2. append new row to output
        """
        if numRows == 0:
            return []
        output = [[1]]
        for i in range(1,numRows):
            new_r = [1]
            for j in range(1, i):
                new_r.append(output[i-1][j-1] + output[i-1][j])
            new_r.append[1]
            output.append(new_r)
        return output




#         # print(numRows, numRows // 2)
#         output = []
#         for i in range(1,numRows+1):
#             row = [1] * i
#             output.append(row)
#         # output = [0]*5

#         # row[0] = 1
#         # print(output)
#         def helper(i,j):
#             # output = []
#             # if i == 0:
#             output[0] = [1]
#             # for i in range(numRows):
#             if j == 0 or j == i:
#                 output[i][j] = 1
#             else:
#                 output[i][j] = helper(i-1,j-1)[i-1][j-1] + helper(i-1,j)[i-1][j]
#             return output
#         helper(numRows-1, numRows // 2)
#         # for j in range(1, numRows-1):
#             # output[numRows-1][j] = output[numRows-1][j-1] + output[numRows-1][j]
#         return output
