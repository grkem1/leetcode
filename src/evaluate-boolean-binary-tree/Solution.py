// https://leetcode.com/problems/evaluate-boolean-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if(root.left):
            if(root.val == 2):
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            else:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        else:
            return root.val == 1