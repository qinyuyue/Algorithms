## Move zeroes

class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # n = len(nums)
        # counts = 0
        # while i < n:
        #     if nums[i] == 0:
        #         out = nums.pop(i)
        #         counts += 1
        #         n -= 1
        #         nums.append(0)
        #     else:
        #         i += 1
        # # print(nums)

        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        nums[i:] = [0] * (len(nums) - i)
