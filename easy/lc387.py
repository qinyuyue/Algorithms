# first index of unique string 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ## 98% speed, because the built in function s.count() write by c
        # letters='abcdefghijklmnopqrstuvwxyz'
        # index=[s.index(l) for l in letters if s.count(l) == 1]
        # return min(index) if len(index) > 0 else -1

        # hashmapj, 54%
        dicts = {}
        s = list(s)
        for i in s:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
        for i in range(len(s)):
            if dicts[s[i]] == 1:
                return i
        return -1


        ## run out of time
        # for i in range(len(s)):
        #     if s.count(s[i]) == 1:
        #         return i
        # return -1
