# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        q = [root]
        new_q = []
        while len(q) > 0:
            n = q.pop()
            if n.left:
                new_q.append(n.right)
                new_q.append(n.left)
            if len(q) == 0:
                q = new_q
                if level % 2 == 0:
                    for i in range(len(q) // 2):
                        q[i].val, q[len(q) - i - 1].val = (
                            q[len(q) - i - 1].val,
                            q[i].val,
                        )
                new_q = []
                level += 1
        return root
