# https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def dfs(node):
            nonlocal total,low,high
            if(not node): return
            if(low <= node.val <= high):
                total += node.val
                dfs(node.left)
                dfs(node.right)
            if(low > node.val):
                dfs(node.right)
            if(high < node.val):
                dfs(node.left)
        dfs(root)
        return total