## At least twice of other numbers
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        else:
            max2 = len(nums) -1
            max1 = 0

            for i in range(1,len(nums)):
                if nums[i] > nums[max1]:
                    max2 = max1
                    max1 = i
                    # print(i, nums[max1], nums[max2])
                elif nums[i] > nums[max2]:
                    max2 = i
                # print(i, nums[max1], nums[max2])

            if nums[max1] >= 2 * nums[max2]:
                # print(max1)
                return max1
        return -1
