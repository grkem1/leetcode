// https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        best = 10**5
        prev = -10**5
        def dfs(n):
            nonlocal best, prev
            if(n.left):
                dfs(n.left)
            best = min(best, n.val - prev)
            prev = n.val
            if(n.right):
                dfs(n.right)
        dfs(root)
        return best