# https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        fresh = set()
        rotten = []
        for i,row in enumerate(grid):
            for j,state in enumerate(row):
                if(state == 1): 
                    fresh.add( (i,j) )
                elif(state == 2): 
                    rotten.append( (i,j) )
        if(len(fresh) == 0): 
            return 0
        if(len(rotten) == 0): 
            return -1
        count = 0 
        while(len(rotten)>0 and len(fresh)>0):
            count+=1
            new_rotten = []
            for r in rotten:
                for (i,j) in ( (-1,0),(0,1),(0,-1),(1,0) ):
                    neighbor = (r[0]+i,r[1]+j)
                    if( neighbor in fresh ):
                        new_rotten.append(neighbor)
                        fresh.remove(neighbor)
            rotten = new_rotten
#            print(rotten)
        if(len(fresh) != 0): 
            return -1
        else:
            return count
