# from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        """
        Algorithms:
        1. initialize an empty queue
        2. find root: for each item in array:
            if item == 0, put it in to queue.
        3. for item in queue, start searching:
            if item == inf, 
            item = minimize of branch or current value
            add item to queue
        """
        if len(rooms) > 0:
            nr = len(rooms)
            nc = len(rooms[0])
            queue = []
            inf = 2 ** 31 - 1
            # print(inf)
            for i in range(nr):
                for j in range(nc):
                    if rooms[i][j] == 0:
                        queue.append((i,j))
            # print(queue)
            while len(queue) > 0:
                # print("queue", queue)
                i,j = queue.pop(0)
                curr = rooms[i][j]

                # print("i,j", i,j)
                idx = [(i-1, j), (i+1, j), (i,j-1), (i, j+1)]
                # print("idx", idx)
                children = [item for item in idx if 0<= item[0]< nr and 0<= item[1]< nc and rooms[item[0]][item[1]] == inf]
                # print("children", children)

                for c in children:
                    # rooms[item[0]][item[1]]
                    rooms[c[0]][c[1]] = min(rooms[c[0]][c[1]], curr +1)
                    queue.append(c)
                # print("rooms", rooms)
