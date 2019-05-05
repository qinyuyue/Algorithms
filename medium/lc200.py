## Number of Island 
"""
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
