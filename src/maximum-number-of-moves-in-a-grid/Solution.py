# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        best = 0
        seen = dict()
        def dfs(i,j):
            nonlocal best, seen
            if((i,j) in seen):
                return seen[(i,j)]
            current = 0
            if(i > 0 and j < len(grid[0])-1 and grid[i][j] < grid[i-1][j+1]):
                current = max(current, dfs(i-1, j+1)+1)
            if(j < len(grid[0])-1 and grid[i][j] < grid[i][j+1]):
                current = max(current, dfs(i, j+1)+1)
            if(i < len(grid)-1 and j < len(grid[0])-1 and grid[i][j] < grid[i+1][j+1]):
                current = max(current, dfs(i+1, j+1)+1)
            # print(i,j)
            seen[(i,j)] = current
            best = max(best, current)
            return current
        for i in range(len(grid)):
            dfs(i,0)
        return best
