# https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy = dummy_head
        current = head
        while(current):
            if(current.next == None or current.next.val != current.val):
                dummy.next = current
                dummy = dummy.next
            current = current.next
        return dummy_head.next