## Array Partition I

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # sort_nums = sorted(nums)
        # # print(sort_nums)
        # sums = 0
        # for i in range(len(sort_nums)):
        #     if i % 2 == 0:
        #         # print(i, sort_nums[i])
        #         sums += sort_nums[i]
        #         # print(sums)
        # return sums

        sums = 0
        if nums:
            nums = sorted(nums)
            odd = False
            i = 0
            j = len(nums) - 2
            n = len(nums) // 2
            if n % 2 == 1:
                odd = True
            while i < j:
                sums += nums[i]
                sums += nums[j]
                i += 2
                j -= 2
            if odd == True:
                sums += nums[i]
        return sums

                
