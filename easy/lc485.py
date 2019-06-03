## Find Max Consecutive Ones 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Two pointer, i is left of 1s, j is right of 1s. maxs = max(j-i, maxs)
        if meet 0, j move until find next 1, i = j
        """
        i = 0
        j = 0
        maxs = 0
        while j < len(nums):
            # print(j)
            if nums[j] == 1:
                i = j
                while j+1 < len(nums) and nums[j+1] == 1:
                    j += 1
                    # print("w", j)
                # j += 1
                maxs = max(maxs, j-i+1)
            j += 1
        return maxs
