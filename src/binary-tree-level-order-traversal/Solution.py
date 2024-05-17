# https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root == None): return []
        values = [[]]
        v_count = 0
        remaining = 1
        level = 0
        nodes = [root]
        for n in nodes:
            if(remaining == 0):
                values.append([])
                level += 1
                remaining = len(nodes) - v_count
            values[level].append(n.val)
            v_count += 1
            if(n.left): nodes.append(n.left)
            if(n.right): nodes.append(n.right)
            remaining -= 1
        return values