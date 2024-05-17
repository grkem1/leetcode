# https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        number = 0
        def dfs(n):
            nonlocal total,number
            if(not n.left and not n.right):
                total += 10 * number + n.val
                return
            number = number * 10 + n.val
            if(n.left):dfs(n.left)
            if(n.right):dfs(n.right)
            number //= 10
        dfs(root)
        return total