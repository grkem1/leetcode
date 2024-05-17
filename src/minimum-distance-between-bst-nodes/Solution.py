# https://leetcode.com/problems/minimum-distance-between-bst-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        best = 10**5
        last = -10**5
        def dfs(n):
            nonlocal best,last
            if(not n): return
            dfs(n.left)
            best = min(best,n.val - last)
            last = n.val
            dfs(n.right)
        dfs(root)
        return best