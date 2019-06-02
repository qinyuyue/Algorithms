# Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Algorithm
        1. m, n is the length of haystack and needle, separately
        2. iterate haystack, if haystack[i:i+n] == needle, return 0
        3. return -1
        """
        if haystack == needle:
            return 0
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i

        return -1

        """
        Algorithm:
        1. m, n is the length of haystack and needle, separately
        2. iterate haystack, if current char == needle[0]
            if haystack[i:i+n] == needle, return 0
        3. return -1
        """
#         if haystack == needle:
#             return 0
#         if needle == '':
#             return 0
#         m = len(haystack)
#         n = len(needle)
#         for i in range(m-n+1):
#             if haystack[i] == needle[0]:
#                 if haystack[i:i+n] == needle:
#                     return i

#         return -1
