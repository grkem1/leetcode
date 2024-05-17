# https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        l = right-left+1
        if(l <= 1): return head
        s = []
        c = head
        for i in range(left-1):
            c = c.next
        d = c
        for i in range(l):
            s.append(d.val)
            d = d.next
        for i in range(l):
            c.val = s.pop()
            c = c.next
        return head