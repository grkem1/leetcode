# https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if(not root): return []
        result = []
        def dfs(n):
            nonlocal result
            for c in n.children:
                dfs(c)
            result.append(n.val)
        dfs(root)
        return result
