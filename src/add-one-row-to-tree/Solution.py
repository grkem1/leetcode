// https://leetcode.com/problems/add-one-row-to-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        nodes = deque()
        def findNodes(current=None,to_go=1):
            if(to_go == 0):
                nodes.append(current)
            if(current.left): findNodes(current.left,to_go-1)
            if(current.right): findNodes(current.right,to_go-1)
        d = d - 2
        if(d == -1):
            return TreeNode(v,root,None)
        findNodes(root,to_go=d)
        for n in nodes:
            left,right = TreeNode(v,n.left,None), TreeNode(v,None,n.right)
            n.left = left
            n.right = right
        return root