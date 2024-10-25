# https://leetcode.com/problems/cousins-in-binary-tree-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = collections.deque([root, None])
        while(len(nodes) > 1):
            level = 0
            for n in nodes:
                if(not n):
                    break
                if(n.left):
                    level += n.left.val
                if(n.right):
                    level += n.right.val
            while(n := nodes.popleft()):
                cousins = 0
                if(n.left):
                    cousins += n.left.val
                if(n.right):
                    cousins += n.right.val
                if(n.left):
                    n.left.val = level - cousins
                    nodes.append(n.left)
                if(n.right):
                    n.right.val = level - cousins
                    nodes.append(n.right)
            nodes.append(None)
        root.val = 0
        return root
