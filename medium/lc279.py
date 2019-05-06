## Perfect Square 

class Solution:
    def numSquares(self, n: int) -> int:

        """
        1. initilize a queue, put (target,level = 0) in
        2. while queue > 0, pop head i out of queue, get the max square root of i.
            for each root < i:
                check (target - i ** 2):
                if it is a square number return level + 1
                else: add it to the queue
        """
        if n == 0:
            return 0
        queue = collections.deque([(n, 0)])
        def isSqure(x):
            if int((x ** 0.5).real)** 2 == x:
                return True
        while len(queue)>0:
            node = queue.popleft()
            if isSqure(node[0]):
                return node[1] + 1
            num, level = int((node[0] ** 0.5).real), node[1]
            for i in range(num, 0, -1):
                comp = node[0] - i**2
                queue.append((comp, level + 1))
