// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if(len(preorder) == 0 or len(inorder) == 0): return None
        head = preorder[0]
        mid_index = inorder.index(head)
        left_preorder = []; right_preorder = []
        left_inorder_set = set(inorder[:mid_index])
        for i in preorder[1:]:
            if(i in left_inorder_set):
                left_preorder.append(i)
            else:
                right_preorder.append(i)
        return TreeNode(head,self.buildTree(left_preorder,inorder[:mid_index]),self.buildTree(right_preorder,inorder[mid_index+1:]))