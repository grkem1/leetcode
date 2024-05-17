# https://leetcode.com/problems/island-perimeter

class Solution:
    def islandPerimeter(self, grid: [[int]]) -> int:
        t = 0 
        for row in grid:
            last = 0 
            for el in row:
                if(el!=last):
                    t+=1
                    last = el
        t+=sum(row[-1] for row in grid)
        for i in range(len(grid[0])):
            last = 0 
            for j in range(len(grid)):
                if(last!=grid[j][i]):
                    t+=1
                    last = grid[j][i]
        t+=sum(grid[-1])
        return t