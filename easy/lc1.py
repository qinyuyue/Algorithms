## Two sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Algorithm - HashMap 
        """
        dic = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] not in dic:
                dic[comp] = i
            else:
                return [dic[nums[i]], i]
