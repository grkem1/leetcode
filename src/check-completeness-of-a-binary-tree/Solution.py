# https://leetcode.com/problems/check-completeness-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        q_new = deque()
        seen_none = False
        while(len(q) > 0):
            n = q.popleft()
            if(n and seen_none):
                return False
            if(not n):
                seen_none = True
            else:
                q_new.append(n.left)
                q_new.append(n.right)
            if(len(q) == 0):
                q = q_new
                q_new = deque()
        return True