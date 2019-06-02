## Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Algorithm:
        1. go through once, find the minimal length of string
        2. i as index of min_str, for each item in strs, check every item equal to min_str[i] or not
        """
        if strs:
            mins = float('inf')
            for i in range(len(strs)):
                if len(strs[i]) < mins:
                    mins = len(strs[i])
                    index = i
            min_s = strs[index]
            j = 0
            while j < len(min_s):
                for item in strs:
                    if item[j] != min_s[j]:
                        return min_s[:j]
                j += 1
            ## if min_s is the common length
            if j == mins:
                return min_s
        return ''
