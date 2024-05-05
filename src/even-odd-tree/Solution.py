// https://leetcode.com/problems/even-odd-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root, None])
        odd = True
        last = 0
        while(len(q) > 1):
            node = q.popleft()
            if(node == None):
                odd = not odd
                last = 0 if odd else 10**6+1
                q.append(None)
                continue
            if(odd and ( node.val <= last or node.val %2 == 0 ) ):
                return False
            if(not odd and ( node.val >= last or node.val %2 == 1 ) ):
                return False
            last = node.val
            if(node.left): q.append(node.left)
            if(node.right): q.append(node.right)
        return True