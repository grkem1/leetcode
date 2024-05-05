// https://leetcode.com/problems/maximum-width-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = collections.defaultdict(list)
        def dfs(node,val,level):
            nonlocal levels
            if(node == None): return
            levels[level].append(val)
            dfs(node.left,2*val,level+1)
            dfs(node.right,2*val+1,level+1)
            return
        dfs(root,0,0)
        max_breadth = 1
        for level in levels:
            max_breadth = max(max_breadth,levels[level][-1]-levels[level][0]+1)
        return max_breadth