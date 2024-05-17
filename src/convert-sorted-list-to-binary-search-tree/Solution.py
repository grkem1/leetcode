# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        l = []
        while(head):
            l.append(head.val)
            head = head.next
        def construct_tree(start,end):
            nonlocal l
            if(start > end): return None
            mid = (start + end) // 2
            top = TreeNode(val = l[mid], left = construct_tree(start,mid-1), right = construct_tree(mid+1,end))
            return top
        return construct_tree(0,len(l)-1)