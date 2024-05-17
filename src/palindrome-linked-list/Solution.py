# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(not head or not head.next):
            return True
        def dfs(node):
            if(not node.next):
                if(head.val == node.val):
                    return head.next
                else:
                    return False
            else:
                counterpart = dfs(node.next)
                if(counterpart == False or counterpart.val != node.val):
                    return False
                return counterpart.next if counterpart.next else True
        return dfs(head)