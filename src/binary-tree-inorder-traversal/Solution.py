# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if(root == None): return []
        return_list = [root.val]
        if(root.left != None): return_list = self.inorderTraversal(root.left) + return_list
        if(root.right != None): return_list = return_list + self.inorderTraversal(root.right)
        return return_list