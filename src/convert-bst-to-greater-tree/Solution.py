// https://leetcode.com/problems/convert-bst-to-greater-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def calc_sum(node,offset=0):
            if(node == None): return 0
            s_right = calc_sum(node.right,offset) + node.val
            s_left  = calc_sum(node.left,s_right + offset)
            node.val = s_right + offset
            return s_right + s_left
        calc_sum(root)
        return root