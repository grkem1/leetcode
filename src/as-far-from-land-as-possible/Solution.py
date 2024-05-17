# https://leetcode.com/problems/as-far-from-land-as-possible

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        for i,r in enumerate(grid):
            for j,c in enumerate(r):
                if(c == 1):
                    q.append( (i,j) )
        if(len(q) in (0,n*n)):
            return -1
        level = 1
        q.append( (-1,-1) )
        # print(q)
        while( len(q) > 1 ):
            # print(q)
            i,j = q.popleft()
            if(i == j == -1):
                level += 1
                q.append( (-1,-1) )
            for dirs in ( (-1,0),(1,0),(0,-1),(0,1) ):
                d_i,d_j = dirs
                i_,j_ = i+d_i,j+d_j
                if(-1 < i_ < n and -1 < j_ < n and grid[i_][j_] == 0):
                    grid[i_][j_] = level
                    q.append( (i_,j_) )
        # print(grid)
        return level-1