// https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        last = TreeNode(-2**31)
        unfit = [last]
        def dfs(node):
            nonlocal last
            if(node == None): return
            dfs(node.left)
            if(node.val < last.val):
                if(unfit[-1] != last):
                    unfit.append(last)
                unfit.append(node)
            last = node
            dfs(node.right)
        dfs(root)
        unfit[1].val,unfit[-1].val = unfit[-1].val,unfit[1].val