class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Algorithm:
        1. initialize queue with start
        2. iterate queue, pop out the head, BFS, until head equal to target, return   

        """

        def neighbors(node):
            nei = []
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    neighbor = node[:i] + str((x + d) % 10) + node[i+1:]
                    nei.append(neighbor)
            return nei

        deadends = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = {'0000'}
        while len(queue) > 0:
            psw, level = queue.popleft()
            if psw == target:
                return level
            if psw in deadends:
                continue ## jump out of the loop
            nei = neighbors(psw)
            for n in nei:
                # if n not in deadends and n not in visited:
                if n not in visited:
                    visited.add(n)
                    queue.append((n, level+1))

        return -1
