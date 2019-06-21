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


        """
        Algorithm - fast/slow pointer
        """
        p1 = self.step(n)
        p2 = self.step(p1)
        while p2 != 1:
            if p1 == p2:
                return False
            p1 = self.step(p1)
            p2 = self.step(self.step(p2))
        return True


    def step(self, n):
        sums = 0
        while n > 9:
            sums += ( n % 10 ) ** 2
            res = n // 10
            n = res
        sums += n ** 2
        return sums
