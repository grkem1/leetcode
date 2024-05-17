# https://leetcode.com/problems/n-ary-tree-level-order-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if(root == None):return []
        levels = []
        level = [root]
        while(len(level)>0):
            levels.append([n.val for n in level])
            new_level = []
            for n in level:
                if(n.children): new_level += n.children
            level = new_level
        return levels