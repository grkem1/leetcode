# https://leetcode.com/problems/largest-plus-sign

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: [[int]]) -> int:
        grid = [[1]*n for i in range(n)]
        for m in mines:
            grid[m[0]][m[1]]=0
        dp = [[n for i in range(n)] for j in range(n)]
        for r in range(n):
            val = 1 
            for c in range(n):
                if(grid[r][c]==0):
                    val=0
                dp[r][c]=val
                val+=1
        for r in range(n):
            val = 1 
            for c in range(n-1,-1,-1):
                if(grid[r][c]==0):
                    val=0
                dp[r][c]=min(val,dp[r][c])
                val+=1
        for c in range(n):
            val = 1 
            for r in range(n):
                if(grid[r][c]==0):
                    val=0
                dp[r][c]=min(val,dp[r][c])
                val+=1
        k=0 
        for c in range(n):
            val = 1 
            for r in range(n-1,-1,-1):
                if(grid[r][c]==0):
                    val=0
                dp[r][c]=min(val,dp[r][c])
                k = max(k,dp[r][c])
                val+=1
        return k