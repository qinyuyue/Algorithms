## Number of Island
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        BFS
        Algorithms:
        1. initialize queue, count += 1
        2. iterate each i in grid,
            if i == 1, add to queue, count += 1
        3. write bsf function
        """
        count = 0
        if len(grid) > 0:
            nr = len(grid)
            nc = len(grid[0])
            q = []

            def BFS():
                while len(q) > 0:
                    i, j = q.pop(0)
                    if i-1 >= 0 and grid[i-1][j] == '1':
                        q.append((i-1,j))
                        grid[i-1][j] = '0'
                    if i+1 < nr and grid[i+1][j] == '1':
                        q.append((i+1,j))
                        grid[i+1][j] = '0'
                    if j-1 >= 0 and grid[i][j-1] == '1':
                        q.append((i,j-1))
                        grid[i][j-1] = '0'
                    if j+1 < nc and grid[i][j+1] == '1':
                        q.append((i,j+1))
                        grid[i][j+1] = '0'

            for i in range(nr):
                for j in range(nc):
                    if grid[i][j] == '1':
                        q.append((i,j))
                        count += 1
                        BFS()


        return count


        """
        DFS 81%
        Algorithms:
        1. define DFS function, if 4 direction are in boarder, change current cell to 0, call DFS function with four directions
        2. iterate every node in grid, if grid[icall DFS function, and count += 1
        """


        c = 0
        if grid:
            nr = len(grid)
            nc = len(grid[0])

            def DFS(grid, i, j):
                # print(grid, i, j)
                if i>=0 and j>= 0 and i<nr and j<nc and grid[i][j] == '1':
                # if i<0 or j< 0 or i >= nr or j>= nc or grid[i][j] != '1':
                    # return
                    grid[i][j] = '0'
                    DFS(grid,i-1,j)
                    DFS(grid,i,j-1)
                    DFS(grid,i+1,j)
                    DFS(grid,i,j+1)
                # else:
                #     return;

            for i in range(nr):
                for j in range(nc):
                    if grid[i][j] == '1':
                        DFS(grid, i, j)
                        c += 1
        return c
