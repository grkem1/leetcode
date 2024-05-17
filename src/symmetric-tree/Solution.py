# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(not root.right and not root.left):
            return True
        def traverse(left,right):
            if(bool(left.left) != bool(right.right) or bool(left.right) != bool(right.left)): return False
            if(left.left):
                if(right.right.val != left.left.val): return False
                if(not traverse(left.left,right.right)): return False
            if(left.right):
                if(left.right.val != right.left.val): return False
                if(not traverse(left.right,right.left)): return False
            return True
        return traverse(root,root)