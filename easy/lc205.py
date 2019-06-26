## Isomorphic String
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        """
        Algorithm - two hashmap
        """
#         if len(s) != len(t):
#             return False
#         dic1 = {}
#         dic2 = {}
#         for i in range(len(s)):
#             if s[i] not in dic1 and t[i] not in dic2:
#                 dic1[s[i]] = t[i]
#                 dic2[t[i]] = s[i]
#             else:
#                 if s[i] not in dic1 or t[i] not in dic2:
#                     return False
#                 if dic1[s[i]] != t[i] or dic2[t[i]] != s[i]:
#                     return False
#         return True

        """
        Algorithm - set 
        """
        if len(set(s)) == len(set(t)) == len(set(zip(s,t))):
            return True
        return False
