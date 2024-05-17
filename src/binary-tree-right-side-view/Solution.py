# https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        seen = []
        def dfs(node,level=0):
            nonlocal seen
            if(node == None):return
            if(level >= len(seen)):
                seen.append(node.val)
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        dfs(root)
        return seen