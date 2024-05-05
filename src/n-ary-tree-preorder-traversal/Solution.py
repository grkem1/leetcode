// https://leetcode.com/problems/n-ary-tree-preorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l = []
        def traverse(n):
            if(n == None):return
            nonlocal l
            l += [n.val]
            if(n.children):
                for c in n.children:
                    traverse(c)
        if(root): traverse(root)
        return l