## Reserve String 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
#         def helper(start, end, ls):
#             if start >= end:
#                 return

#             ls[start], ls[end] = ls[end], ls[start]

#             return helper(start+1, end-1, ls)

#         helper(0, len(s)-1, s)

        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
