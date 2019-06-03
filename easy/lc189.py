## Rotate array 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        3 steps
        Time O(n), space O(1)
        """
        n = len(nums)
        k = k % n
        self.reverse_arr(nums, 0, n-k-1)
        self.reverse_arr(nums, n-k, n-1)
        self.reverse_arr(nums, 0, n-1)
        # print(nums)

    def reverse_arr(self,arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

        """
        extra space
        Time O(n), space O(n)
        """
        # n = len(nums)
        # k = k % n
        # left = nums[:n-k]
        # right = nums[n-k:]
        # for i in range(k):
        #     print(nums[i], right[i])
        #     nums[i] = right[i]
        # print(nums)
        # print(left)
        # for j in range(k, n):
        #     print(nums[j])
        #     nums[j] = left[j-k]
