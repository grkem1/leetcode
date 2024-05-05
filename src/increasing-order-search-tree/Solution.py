// https://leetcode.com/problems/increasing-order-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if(root == None):
            return None
        def sort_left_right(node):
            if(node.left == node.right == None):
                return node,node
            left_left = None
            if(node.left):
                left_left,left_right = sort_left_right(node.left)
                left_right.right = node
                node.left = None
            if(node.right):
                right_left,right_right = sort_left_right(node.right)
                node.right = right_left
                right_left.left = None
                return (left_left or node),right_right
            return left_left,node
        new_root,_ = sort_left_right(root)
        return new_root