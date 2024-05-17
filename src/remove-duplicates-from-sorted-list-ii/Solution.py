# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        current = head
        dummy = ListNode(-101,head)
        prev = dummy
        tail = dummy
        while(current):
            if(prev.val == current.val or current.next and current.next.val == current.val):
                # print(current.val)
                tail.next = current.next
            else:
                tail = current
            prev = current
            current = current.next
        return dummy.next