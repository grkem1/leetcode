// https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def goodNodes(self, root: TreeNode, cur_max=-10**4) -> int:
        if(root == None):return 0
        if(root.val >= cur_max):
            cur_max = max(root.val,cur_max)
            self.count+=1
#            print("cur_max:" , cur_max, "root_val:", root.val)
        self.goodNodes(root.left,cur_max)
        self.goodNodes(root.right,cur_max)
        return self.count