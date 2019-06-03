## Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        two pointer, O(n)
        """
        i = j = 0
        sums = 0
        mins = float('inf')
        while j < len(nums):
            sums += nums[j]
            while sums >= s:
                mins = min(mins, j-i+1)
                sums -= nums[i]
                i += 1
            j += 1
        return mins if mins <= len(nums) else 0
