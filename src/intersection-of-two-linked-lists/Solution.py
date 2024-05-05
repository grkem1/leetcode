// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currentA, currentB = headA, headB
        countA = countB = 0
        while(currentA):
            countA += 1
            currentA = currentA.next
        while(currentB):
            countB += 1
            currentB = currentB.next
        currentA, currentB = headA, headB
        difference = countA - countB
        for i in range(difference):
            currentA = currentA.next
        for i in range(-difference):
            currentB = currentB.next
        while(currentA and currentB):
            if(currentA == currentB):
                return currentA
            currentA = currentA.next
            currentB = currentB.next
        return None
        