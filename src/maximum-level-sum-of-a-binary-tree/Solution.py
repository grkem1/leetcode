// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        current = 0
        best = -10**10
        best_level = 1
        nodes = deque()
        nodes.append(root)
        nodes.append(None)
        while(len(nodes) > 1):
            n = nodes.popleft()
            if(n == None):
                if(best < current):
                    best = current
                    best_level = level
                current = 0
                nodes.append(None)
                level += 1
                continue
            current += n.val
            if(n.left): nodes.append(n.left)
            if(n.right): nodes.append(n.right)
        if(current > best):
            best_level = level
        return best_level