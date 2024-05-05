// https://leetcode.com/problems/binary-tree-cameras

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        count = 0
        def recurse(start: TreeNode):
            nonlocal count
            if(start == None): return -1 # leaf
            l = recurse(start.left)
            r = recurse(start.right)
            if(l == r == -1): return 0
            if(l == 0 or r == 0):
                count += 1
                return 2
            if(l == 2 or r == 2):
                return 1
            return 0  
        recurse(TreeNode(left=root))
        return count