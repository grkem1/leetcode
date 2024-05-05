// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node_original,node_copy):
            nonlocal target
            if(node_original == None):
                return None
            if(node_original == target):
                return node_copy
            left = dfs(node_original.left,node_copy.left)
            right = dfs(node_original.right,node_copy.right)
            return left or right
        return dfs(original,cloned)