// https://leetcode.com/problems/cousins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        level_x,level_y,parent_x,parent_y=-1,-1,-1,-1
        def dfs(node=root,level=0):
            nonlocal x,y,level_x,level_y,parent_x,parent_y
            level+=1
            if(node.left!=None):
                if(node.left.val == x):
                    parent_x = node.val
                    level_x = level
                    if(level_y != -1):
                        return True
                elif(node.left.val == y):
                    parent_y = node.val
                    level_y = level
                    if(level_x != -1):
                        return True
                else:
                    dfs(node.left,level)
            if(node.right!=None):
                if(node.right.val == x):
                    parent_x = node.val
                    level_x = level
                    if(level_y != -1):
                        return True
                elif(node.right.val == y):
                    parent_y = node.val
                    level_y = level
                    if(level_x != -1):
                        return True
                else:
                    dfs(node.right,level)
        if(root.val == x or root.val == y):return False
        dfs()
        return ( (level_x == level_y) and (parent_x != parent_y) )