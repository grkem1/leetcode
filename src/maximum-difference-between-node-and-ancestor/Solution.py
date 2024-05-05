// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_min = [(root.val,root.val)]
        best = 0
        def dfs(n):
            nonlocal best, max_min
            best = max(best, max(abs(n.val - max_min[-1][0]),abs(n.val - max_min[-1][1])))
            max_min.append( (max( max_min[-1][0],n.val ) , min( max_min[-1][1],n.val )) )
            if(n.right):
                dfs(n.right)
            if(n.left):
                dfs(n.left)
            max_min.pop()
        dfs(root)
        return best