// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, grid: [[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [1]*n
        for i,el in enumerate(grid[0]):
            if(el == 1): # there is a block at i
                for j in range(i,n):
                    dp[j] = 0
                break
        for i in range(1,m):
            # print(dp)
            dp[0] = dp[0] if grid[i][0] == 0 else 0
            for j in range(1,n):
                dp[j] = dp[j-1] + dp[j] if grid[i][j] == 0 else 0
            # print(dp)
        return dp[-1]
        