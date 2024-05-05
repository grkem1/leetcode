// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_found = False
        q_found = False
        stack = []
        p_stack = None
        q_stack = None
        def find_pq(node):
            nonlocal p,q,stack,p_stack,q_stack,p_found,q_found
            if(node == None):
                return
            if(node == p):
                p_found = True
                p_stack = stack.copy()
            elif(node == q):
                q_found = True
                q_stack = stack.copy()
            if(p_found and q_found):
                return
            stack.append(False)
            find_pq(node.left)
            stack.pop()
            stack.append(True)
            find_pq(node.right)
            stack.pop()
        find_pq(root)
        common = root
        for i,j in zip(p_stack,q_stack):
            if(i != j):
                break
            if(i == True):
                common = common.right
            else:
                common = common.left
        return common