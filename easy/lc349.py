## Intersection of two arrays 

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        output = set()
        for i in set2:
            if i in set1:
                output.add(i)
        return list(output)
