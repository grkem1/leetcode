// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        total = 0
        if(root == None): return total
        def dfs(node):
            nonlocal total
            children_count = 1
            children_toplam = node.val
            if(node.left):
                t,c = dfs(node.left)
                children_count += c
                children_toplam += t
            if(node.right):
                t,c = dfs(node.right)
                children_count += c
                children_toplam += t
            # print(node.val, children_toplam, children_count)
            if(children_toplam // children_count == node.val):
                total += 1
            return (children_toplam, children_count)
        dfs(root)
        return total