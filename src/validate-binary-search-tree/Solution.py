// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bst = True
        def dfs(node):
            nonlocal bst
            s = l = node.val
            if(node.left):
                s,s_l = dfs(node.left)
                if(s_l >= node.val):
                    bst = False
                    return s,l
            if(node.right):
                l_s,l = dfs(node.right)
                if(l_s <= node.val):
                    bst = False
                    return s,l
            return s,l
        dfs(root)
        return bst