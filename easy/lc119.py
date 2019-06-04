## Pascal Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
######### recursion I ############
#         def helper(num):
#             if num == 0:
#                 output = [1]
#             else:
#                 prev = helper(num-1)
#                 output = [1,1]
#                 for j in range(1, num):
#                     output.insert(j, (prev[j-1] + prev[j]))
#             return output
#         return helper(rowIndex)

######### recursion II #############
        # def helper(num):
        #     if num  == 1:
        #         output = [[1]]
        #     else:
        #         output = helper(num-1)
        #         pre_row = output[-1]
        #         cur_row = []
        #         for j in range(num):
        #             if j == 0:
        #                 cur_row.append(1)
        #             elif j < (num -1):
        #                 cur_row.append(pre_row[j-1] + pre_row[j])
        #             else:
        #                 cur_row.append(1)
        #         output.append(cur_row)
        #     return output
        # return helper(rowIndex+1)[-1]

        last = [1]
        curr = [1]
        for i in range(1, rowIndex+1):
            for j in range(i-1):
                curr.append((last[j]+last[j+1]))
            curr.append(1)
            last = curr
            curr = [1]
        return last
