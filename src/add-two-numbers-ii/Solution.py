// https://leetcode.com/problems/add-two-numbers-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        i1 = 0
        while(n1):
            i1 *= 10
            i1 += n1.val
            n1 = n1.next
        n2 = l2
        i2 = 0
        while(n2):
            i2 *= 10
            i2 += n2.val
            n2 = n2.next
        i3 = i1 + i2
        if(i3 == 0): return ListNode(0)
        l3 = ListNode()
        while(i3 > 0):
            n = ListNode(i3%10,l3.next)
            i3 //= 10
            l3.next = n
        return l3.next