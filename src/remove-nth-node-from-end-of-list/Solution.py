// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if(head.next == None): return None
        nth = last = ListNode(0,head)
        for i in range(n): # leave gap of n between last
            last = last.next
        if(last.next == None): return head.next
        while(last.next):  # find last and nth
            last = last.next
            nth = nth.next
        nth.next = nth.next.next # remove nth
        return head