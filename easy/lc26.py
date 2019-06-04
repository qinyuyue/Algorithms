## Remove Duplicates

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#         orginal one, remove list
        # i = 1
        # lens = len(nums)
        # while i < lens:
        #     if nums[i] == nums[i-1]:
        #         nums.pop(i)
        #         lens = len(nums)
        #     else:
        #         i += 1
        # return len(nums)

        lenOfNew = 0
        for i in range(len(nums)):
            if nums[i] != nums[lenOfNew]:
                lenOfNew += 1
                nums[lenOfNew] = nums[i]
        # print(lenOfNew)

        return lenOfNew+1 if nums else 0
