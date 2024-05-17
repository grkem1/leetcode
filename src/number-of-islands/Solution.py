# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        def return_neighbors(i,j):
            nonlocal m,n,grid
            if((not 0 <= i < m) or (not 0 <= j < n) or (grid[i][j] == "0")): return False
            grid[i][j] = "0"
            for i_,j_ in ((-1,0),(1,0),(0,-1),(0,1)):
                return_neighbors(i+i_,j+j_)
            return True
        total = 0
        for r in range(m):
            for c in range(n):
                if(return_neighbors(r,c)):
                    total += 1
        return total