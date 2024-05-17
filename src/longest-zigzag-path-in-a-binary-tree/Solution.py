# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        best = 0
        def dfs(node):
            nonlocal best
            l = r = 0
            if(node.left):
                l = dfs(node.left)[1] + 1
            if(node.right):
                r = dfs(node.right)[0] + 1
            best = max(best,l,r)
            return (l,r)
        dfs(root)
        return best