// https://leetcode.com/problems/out-of-boundary-paths

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        grid = [[0]*(n+2) for i in range(m+2)]
        grid[startRow+1][startColumn+1] = 1
        for move in range(maxMove):
            # print(grid)
            new_grid = [[0]*(n+2) for i in range(m+2)]
            new_grid[0] = grid[0].copy()
            new_grid[-1] = grid[-1].copy()
            for i in range(1,m+1):
                new_grid[i][0] = grid[i][0]
                new_grid[i][-1] = grid[i][-1]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if(grid[i][j] > 0):
                        new_grid[i-1][j] += grid[i][j]
                        new_grid[i][j-1] += grid[i][j]
                        new_grid[i+1][j] += grid[i][j]
                        new_grid[i][j+1] += grid[i][j]
            grid = new_grid
        # print(grid)
        return (sum(grid[0]) + sum(grid[-1]) + sum(grid[i][0]+grid[i][-1] for i in range(1,m+1)))%(10**9+7)