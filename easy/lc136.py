## single number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        """
        Algorithm - Hashset
        TO(n), SO(n)
        """
        # sets = set()
        # for i in nums:
        #     if i not in sets:
        #         sets.add(i)
        #     else:
        #         sets.remove(i)
        # x = sets.pop()
        # return x

        """
        Algorithm - Bit Manipulation
        TO(n), SO(1)
        """
        a = 0
        for i in nums:
            a ^= i
        return a 
