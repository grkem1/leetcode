// https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(r,tS,path):
            nonlocal paths
            if(r.left):
                dfs(r.left,tS-r.val,path+[r.val])
            if(r.right):
                dfs(r.right,tS-r.val,path+[r.val])
            elif(r.left == None and r.val == tS):
                paths.append(path+[r.val])
        if(root == None): return paths
        dfs(root,targetSum,[])
        return paths
