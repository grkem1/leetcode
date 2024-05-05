// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if(root == None): return 0
        dummy = root
        level = 0
        while(dummy):
            dummy = dummy.left
            level += 1
        l,r = 0,2**(level - 1) - 1
        def take_path(x):
            nonlocal root,level
            dummy = root
            for i in range(level-2,-1,-1):
                if(x & (1 << i )):
                    dummy = dummy.right
                else:
                    dummy = dummy.left
                if(not dummy):
                    return False
            return True
        while(l < r - 1):
            m = (l + r)//2
            if(take_path(m)):
                l = m
            else:
                r = m
        if(take_path(r)): l = r
        return 2**(level-1) + l
