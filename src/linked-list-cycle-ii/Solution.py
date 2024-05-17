# https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head): return None
        fast = slow = head
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                break
        if(fast.next == None or fast.next.next == None):
            return None
        new = head
        while(new != slow):
            slow = slow.next
            new = new.next
        return new