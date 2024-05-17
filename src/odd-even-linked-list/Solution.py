# https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head): return head
        cur = head
        evens = head.next
        if(not evens or not evens.next): return head
        i = 0
        while(cur.next and cur.next.next):
            temp = cur.next
            cur.next = cur.next.next
            cur = temp
            #cur,cur.next = cur.next,cur.next.next
            i+=1
        if(i % 2 == 1):
            temp = cur.next
            cur.next = None
            temp.next = evens
        else:
            cur.next = evens
        return head