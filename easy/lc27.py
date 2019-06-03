## Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # lens = len(nums)
        # i = 0
        # while i < lens:
        #     if nums[i] == val:
        #         nums.pop(i)
        #         lens = len(nums)
        #     else:
        #         i += 1
        # return len(nums)

        """
        Two pointer, one from left to right, one from right to left
        if left is val, then swap with right, right --
        else: left ++
        """
        # if not nums:
        #     return 0
        # else:
        #     i = 0
        #     j = len(nums) - 1
        #     k = len(nums) - 1
        #     while i < k:
        #         if nums[i] == val:
        #             nums[i], nums[k] = nums[k], nums[i]
        #             k -= 1
        #         else:
        #             i += 1
        #     if nums[k] != val:
        #         k += 1
        #     return k

        """
        Two pointer, one is quicker one is slower.
        If quicker one is not val, slower equal to quicker, slower ++ 
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
