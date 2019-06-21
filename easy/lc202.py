## Happy Number 

class Solution:
    def isHappy(self, n: int) -> bool:
        if type(n) is int:
            visited = set()
            visited.add(n)
            while n != 1:
                nums = list(str(n))
                new_n = 0
                for i in nums:
                    new_n += int(i) ** 2
                if new_n in visited:
                    return False
                visited.add(new_n)
                n = new_n
            return True
        return False
