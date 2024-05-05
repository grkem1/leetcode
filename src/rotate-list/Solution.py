// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head == None or head.next == None or k == 0):
            return head
        dummy = head
        length = 0
        while(dummy):
            length += 1
            dummy = dummy.next
        k = k % length
        if(k == 0): return head
        lead = lag = head
        for i in range(k):
            lead = lead.next
        while(lead.next):
            lead = lead.next
            lag = lag.next
        lead.next = head
        head = lag.next
        lag.next = None
        return head