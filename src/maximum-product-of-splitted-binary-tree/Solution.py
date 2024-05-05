// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root) -> int:
        total = 0 
        def dfs_sum(r):
            nonlocal total
            if(r == None):return
            total+=r.val
            dfs_sum(r.left)
            dfs_sum(r.right)
        dfs_sum(root)
#        print(total)
        closest = total
        def dfs_subtree(r):
            if(r == None):return 0
            nonlocal closest
            c = r.val
            c += dfs_subtree(r.left)
            c += dfs_subtree(r.right)
            if(abs(total//2 - c) < abs(total//2 - closest)):
                closest = c 
            return c
        dfs_subtree(root)
        return (closest * (total-closest))%(10**9+7)