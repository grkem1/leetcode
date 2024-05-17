# https://leetcode.com/problems/number-of-enclaves

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def walk(i,j):
            nonlocal grid
            if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0):
                return
            grid[i][j] = 0
            for delta in ((-1,0),(0,1),(1,0),(0,-1)):
                walk(i+delta[0],j+delta[1])
        for i in range(len(grid)):
            walk(i,0)
            walk(i,len(grid[0])-1)
        for j in range(len(grid[0])):
            walk(0,j)
            walk(len(grid)-1,j)
        total = 0
        for r in grid:
            total += sum(r)
        print(grid)
        return total