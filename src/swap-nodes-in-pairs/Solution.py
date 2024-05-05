// https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head
        while(current != None and current.next != None):
            current.val,current.next.val = current.next.val,current.val
            current = current.next.next
        return head