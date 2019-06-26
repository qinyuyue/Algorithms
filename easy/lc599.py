# Minimum Index Sum of Two Lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        """
        Algorithm - hashmap
        TO(m+n), SO(min(m,n))
        """
        mins = float('inf')
        key = []
        dic = {k:v for v, k in enumerate(list1)}
        # print(dic)
        for i in range(len(list2)):
            if list2[i] in dic:
                if dic[list2[i]] + i < mins:
                    mins = dic[list2[i]] + i
                    key = [list2[i]]
                elif dic[list2[i]] + i == mins:
                    key.append(list2[i])
        return key
