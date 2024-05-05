// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if(root == None): return None
        self.flatten(root.left)
        self.flatten(root.right)
        if(root.left):
            c = root.left
            while(c.right):
                c = c.right
            c.right = root.right
            root.right = root.left
            root.left = None