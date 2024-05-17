# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # let's waste some memory
        if(not head): return None
        new_head = None
        def rev(node):
            nonlocal new_head
            if(node.next):
                tmp = node.next
                rev(node.next)
                tmp.next = node
            else:
                new_head = node
        rev(head)
        head.next = None
        return new_head