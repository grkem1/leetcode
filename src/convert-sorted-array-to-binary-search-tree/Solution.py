# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(i,j):
            nonlocal nums
            if(i == j): return TreeNode(nums[i])
            elif(i > j): return None
            mid = (i+j)//2
            return TreeNode(nums[mid],dfs(i,mid-1),dfs(mid+1,j))
        return dfs(0,len(nums)-1)