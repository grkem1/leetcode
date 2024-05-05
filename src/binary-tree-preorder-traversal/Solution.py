// https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        def dfs(n):
            nonlocal nodes
            if(n == None):
                return
            nodes.append(n.val)
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return nodes