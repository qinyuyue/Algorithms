## Next permutation 

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ######## pseudocode #########
        ## 1. from the end to start, find the index i which 1 position before the max.
        ## 2. from the end to start, find the index j of the first number greater than nums[i]
        ## 3. swap nums[i] and nums[j],
        ## 4. severse nums between [i+1, j-1]

        ## same to java soulution
        # lens = len(nums)
        # i = lens - 2
        # while i >= 0 and nums[i+1] <= nums[i]:
        #     i -= 1
        # if i >=0:
        #     j = lens - 1
        #     while j >= 0 and nums[j] <= nums[i]:
        #         j -= 1
        #     nums[i], nums[j] = nums[j], nums[i]
        # nums[i+1:] = reversed(nums[i+1:])

        ## 99% fast solution
        i = j = len(nums)-1
        biggest = True # a flag to see if this list is descended.
        while i >=1:
            if nums[i] > nums[i-1]:
                break
            i -= 1

        while j >= i and i!= 0: # i != 0 is important
            if nums[j] > nums[i-1]:
                nums[j], nums[i-1] = nums[i-1], nums[j]
                j = len(nums)
                nums[i:j] = reversed(nums[i:j])
                biggest = False
                break
            j -= 1
        if biggest == True:
            nums.reverse()
