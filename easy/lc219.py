class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## first approach
#         if len(nums) > 1:
#             dic = {}
#             diff = 0
#             for i in range(len(nums)):
#                 if nums[i] not in dic:
#                     dic[nums[i]] = i
#                 else:
#                     diff = i - dic[nums[i]]
#                     if diff <= k:
#                         return True
#                     dic[nums[i]] = i

#         return False

        ## second approach
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
