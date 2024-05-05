// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        result = ListNode()
        result_tail = result
        while(l1 and l2):
            digit = l1.val + l2.val + carry
            carry = (digit > 9)
            if(carry):
                digit -= 10
            result_tail.next = ListNode(digit)
            result_tail = result_tail.next
            l1,l2 = l1.next,l2.next
        remaining = l1 or l2
        while(remaining):
            if(not carry):
                result_tail.next = remaining
                return result.next
            digit = remaining.val + carry
            carry = (digit > 9)
            if(carry):
                digit -= 10
            result_tail.next = ListNode(digit)
            result_tail = result_tail.next
            remaining = remaining.next

        # while(l1):
        #     digit = l1.val + carry
        #     carry = (digit > 9)
        #     if(carry):
        #         digit -= 10
        #     result_tail.next = ListNode(digit)
        #     result_tail = result_tail.next
        #     l1 = l1.next
        # while(l2):
        #     digit = l2.val + carry
        #     carry = (digit > 9)
        #     if(carry):
        #         digit -= 10
        #     result_tail.next = ListNode(digit)
        #     result_tail = result_tail.next
        #     l2 = l2.next
        if(carry):
            result_tail.next = ListNode(1)
        return result.next