"""
Intersection of Two Arrays II
Time: O(n), Space O(n)
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return

        dic = {}
        output = []
        # iterate over first list

        for i in nums1:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        print(dic)
        # iterate over second list
        for i in nums2:
            if i in dic:
                # print(i, dic)
                if dic[i] > 1:
                    dic[i] -= 1
                else:
                    del dic[i]
                output.append(i)
        return output
