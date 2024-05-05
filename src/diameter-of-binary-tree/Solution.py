// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0 
        def dfs(n):
            if(n == None):return 0
            nonlocal d
            l = dfs(n.left)
            r = dfs(n.right)
            d = max(d,r+l)
            return max(l,r)+1
        dfs(root)
        return d
