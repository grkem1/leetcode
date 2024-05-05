// https://leetcode.com/problems/making-a-large-island

class Solution:
    def largestIsland(self, grid: [[int]]) -> int:
        zeros = [] # list of zeros
        islands = [] # list of islands repr. by a set
        n,m = len(grid),len(grid[0])
        def dfs(i,j,label):
            nonlocal grid,n,m,islands
            if(i < 0 or j < 0 or i >= n or j >= m):return
            if(grid[i][j] == 1):
                islands[-1].add((i,j))
                grid[i][j] = label
                dfs(i+1,j,label)
                dfs(i-1,j,label)
                dfs(i,j-1,label)
                dfs(i,j+1,label)

        last_label = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    islands.append(set())
                    dfs(i,j,last_label)
                    last_label += 1
        if(len(islands) == 0):return 1
        if(len(islands) == 1):return min(len(islands[0])+1,n*m)
        m = 0
        # print('grid:',grid)
        # print('islands:',islands)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 0):
                    neighbors = set()
                    if(i < n-1 and grid[i+1][j] != 0):neighbors.add(grid[i+1][j])
                    if(j < n-1 and grid[i][j+1] != 0):neighbors.add(grid[i][j+1])
                    if(i > 0 and grid[i-1][j] != 0  ):neighbors.add(grid[i-1][j])
                    if(j > 0 and grid[i][j-1] != 0  ):neighbors.add(grid[i][j-1])
                    # print('i:',i,'j:',j,'neighbors:',neighbors)
                    m = max(m,sum(len(islands[n-2]) for n in neighbors)+1)
        return m