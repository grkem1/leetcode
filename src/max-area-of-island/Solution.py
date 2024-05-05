// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int: 
        def exploreIsland(i,j):
            nonlocal grid 
            size = 0
            last = collections.deque()
            last.append((i,j))
            while(len(last) > 0):
                l = last.popleft()
                if(grid[l[0]][l[1]]==0):continue
                size += 1 
                grid[l[0]][l[1]] = 0 # don't redo later
                neighbors = ((l[0]+d,l[1]+r) for (d,r) in ((0,1),(0,-1),(1,0),(-1,0)) if len(grid)>l[0]+d>-1 and len(grid[0])>l[1]+r>-1)
                for n in neighbors: last.append(n)
            return size 
        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]>0):
                    e = exploreIsland(i,j)
                    best = max(best,e)
        return best 
