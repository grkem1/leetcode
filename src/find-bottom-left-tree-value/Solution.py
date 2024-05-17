# https://leetcode.com/problems/find-bottom-left-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level = 0
        leftmost = 0
        def dfs(node,curlevel=0):
            nonlocal level,leftmost
            if(curlevel >= level):
                level = curlevel
                leftmost = node.val
            if(node.right):
                dfs(node.right,curlevel+1)
            if(node.left):
                dfs(node.left,curlevel+1)
        dfs(root)
        return leftmost