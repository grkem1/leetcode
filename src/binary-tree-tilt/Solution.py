# https://leetcode.com/problems/binary-tree-tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if(root == None): return 0
        def acc(node):
            if(node == None):
                return 0
            node.val = acc(node.left) + acc(node.right) + node.val
            return node.val
        acc(root)
        total = 0
        def tilt(node):
            nonlocal total
         #   if(node == None):
         #       return 0
            left,right = 0,0
            if(node.left):
                left = node.left.val
                tilt(node.left)
            if(node.right):
                right = node.right.val
                tilt(node.right)
            total += abs(left - right)
        tilt(root)
        return total