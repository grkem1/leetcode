# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(node,number):
            nonlocal s
            if(node == None):
                return False
            number*=2
            number+=node.val
            is_leaf = not dfs(node.left,number)
            is_leaf = not dfs(node.right,number) and is_leaf
            if(is_leaf):
                #print(number)
                s += number
            return True
        dfs(root,0)
        return s