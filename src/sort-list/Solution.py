# https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = []
        current = head
        while(current):
            val.append(current.val)
            current = current.next
        current = head
        for v in sorted(val):
            current.val = v
            current = current.next
        return head