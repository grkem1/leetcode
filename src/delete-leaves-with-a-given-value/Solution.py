# https://leetcode.com/problems/delete-leaves-with-a-given-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # postorder traversal so that parents turned leaves can be deleted
        # return "delete me" signal to the parent
        # create a dummy so that the same rule applies to the root of the tree
        dummy = TreeNode(0,root,None)
        def dfs(n):
            if(n.left):
                if( dfs(n.left) ):
                    n.left = None
            if(n.right):
                if( dfs(n.right) ):
                    n.right = None
            if(n.val == target and not n.left and not n.right):
                return True
            return False
        dfs(dummy)
        return dummy.left
        # Note: removeLeafNodes itself could be defined recursively, without the
        # need for a helper function.
