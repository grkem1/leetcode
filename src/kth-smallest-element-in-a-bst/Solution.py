# https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        kth_val = -1
        def dfs(node):
            nonlocal count,kth_val,k
            if(node == None or count > k): return
            dfs(node.left)
            count += 1
            if(count == k):
                kth_val = node.val
                return
            dfs(node.right)
        dfs(root)
        return kth_val