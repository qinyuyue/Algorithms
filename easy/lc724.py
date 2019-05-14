## Find the pivot index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ## Brute force, run out of time
        # for i in range(len(nums)):
        #     left = sum(nums[:i])
        #     right = sum(nums[i+1:])
        #     if left == right:
        #         return i
        # return -1

        if len(nums) >0 :
            sums = sum(nums)
            left = 0
            for i in range(len(nums)):

                if left == sums - nums[i] - left:
                    return i
                left += nums[i]
        return -1
