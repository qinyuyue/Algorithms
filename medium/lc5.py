class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        """
        Algorithm:
        1. iterate string from i = 0, initialize two pointers, l = r = i, check the max-length duplicates
        2. then check if s[l-1]  == s[r+1]
        3. check if r-l+1 is the maxium length, then store it.
        """
        maxlen = 0
        start = 0
        for i in range(len(s)):
            l = r = i
            ## check duplicate
            while r+1 < len(s) and s[r+1] == s[l]:
                r += 1
            ## check if both sides of duplicate is same
            while l - 1 >= 0 and r + 1 < len(s) and s[l-1] == s[r+1]:

                l -= 1
                r += 1
            if r - l + 1 > maxlen:
                start = l
                maxlen =  r - l + 1

        return s[start: start+maxlen]
