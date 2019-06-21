## Missing Number 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Algorithm - XOR
        TO(n), SO(1)
        """
        a = lens = len(nums)
        for i in range(lens):
            a ^= i
            a ^= nums[i]
        return a
