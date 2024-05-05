// https://leetcode.com/problems/binary-tree-pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if(root == None ):return None
        root.right = self.pruneTree(root.right)
        root.left  = self.pruneTree(root.left)
        if( root.right == None and root.left == None and root.val != 1 ):
            return None
        return root

    def printTree(self, root: TreeNode):
        if(root == None):return
        self.printTree(root.left)
        print(root.val)
        self.printTree(root.right)