# https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        bigger_head = ListNode()
        bigger_last = bigger_head
        last = ListNode(201,head)
        dummy = last
        while(last.next):
            if(last.next.val >= x):
                bigger_last.next = last.next
                bigger_last = bigger_last.next
                last.next = last.next.next
                bigger_last.next = None
            else:
                last = last.next
        last.next = bigger_head.next
        return dummy.next