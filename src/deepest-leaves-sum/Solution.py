# https://leetcode.com/problems/deepest-leaves-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest_level = 0
        deepest_sum = 0
        def dfs(node,level):
            nonlocal deepest_level,deepest_sum
            if(node == None):return
            dfs(node.left,level+1)
            dfs(node.right,level+1)
            if(level == deepest_level):
                deepest_sum += node.val
            elif(level > deepest_level):
                deepest_level = level
                deepest_sum = node.val
        dfs(root,0)
        return deepest_sum