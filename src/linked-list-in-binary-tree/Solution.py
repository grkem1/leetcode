# https://leetcode.com/problems/linked-list-in-binary-tree

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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(t_node, arr=[]):
            nonlocal head
            arr_new = []
            if(not t_node):
                return False
            if(head.val == t_node.val):
                if(head.next == None):
                    return True
                arr_new.append(head.next)
            for l_node in arr:
                if(l_node.val == t_node.val):
                    if(l_node.next == None):
                        return True
                    arr_new.append(l_node.next)
            return dfs(t_node.left, arr_new) or dfs(t_node.right, arr_new)
        return dfs(root)
