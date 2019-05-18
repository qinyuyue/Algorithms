## Climb stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Algorithm:
        1. if 0 < n < 2, return n
        2. else: n = (n-1) + (n-2)

        Attention:
        must define another helper function. cache is stored besides the function.
        Otherwise it wiil run out of time
        """

        # print(n)
        cache = {}
        def helper(n):
            if n in cache:
                return cache[n]
            elif 0 < n < 4:
                result = n
            else:
                result = helper(n-1) + helper(n-2)
            cache[n] = result
            return result
        return helper(n)
