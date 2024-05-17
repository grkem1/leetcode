# https://leetcode.com/problems/construct-quad-tree

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def divide(origin,length):
            nonlocal grid
            # if(length == 1):
            #     return Node(grid[origin[0]][origin[1]] , True, None,None,None,None )
            iL = True
            origin_val = grid[origin[0]][origin[1]]
            for i in range(length):
                for j in range(length):
                    if(grid[origin[0]+i][origin[1]+j] != origin_val):
                        iL = False
                        break
                if(not iL): break
            if(iL): return Node(grid[origin[0]][origin[1]], True, None,None,None,None )
            return Node(1, False, divide(origin,length//2) , divide([origin[0],origin[1]+length//2],length//2 ), divide([origin[0]+length//2,origin[1]], length//2) , divide([origin[0]+length//2,origin[1]+length//2], length//2)  )
        return divide([0,0],len(grid))