# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0,head)
        ptr = dummy
        while(ptr.next):
            if(ptr.next.val in nums):
                ptr.next.next, ptr.next = None, ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next
