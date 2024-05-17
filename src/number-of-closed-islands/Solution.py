# https://leetcode.com/problems/number-of-closed-islands

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        def findIsland(i,j):
            nonlocal grid,m,n
            if(i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 0): return None,None,None,None
            grid[i][j] = 1
            left = right = j
            up = down = i
            for delta in ((-1,0),(1,0),(0,-1),(0,1)):
                left_,right_,up_,down_ = findIsland(i+delta[0],j+delta[1])
                if(left_ != None):
                    left = min(left,left_)
                    right = max(right,right_)
                    up = min(up,up_)
                    down = max(down,down_)
            return (left,right,up,down)
        total = 0
        for i in range(m):
            for j in range(n):
                left,right,up,down = findIsland(i,j)
                if(left and left > 0 and right < n-1 and up > 0 and down < m-1):
                    # print(left,right,up,down)
                    # print(grid)
                    total+=1
        return total