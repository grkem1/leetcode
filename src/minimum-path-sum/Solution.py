# https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        for c in range(1,n):
            grid[0][c] = grid[0][c-1]+grid[0][c]
        for r in range(1,m):
            grid[r][0] = grid[r-1][0]+grid[r][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]