# https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(not root): return 0
        depth = 1
        q = deque([root, None])
        while(True):
            n = q.popleft()
            if(n == None):
                q.append(None)
                depth+=1
                continue
            if(not n.left and not n.right):
                return depth
            if(n.left):
                q.append(n.left)
            if(n.right):
                q.append(n.right)
        return depth