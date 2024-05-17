# https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if(k == 1): return head
        t = head
        a = []
        b = []
        sz = 0
        while(t):
            if(sz % k == 0): a.append(t)
            if(sz % k == k-1): b.append(t)
            sz += 1
            t = t.next
        prev = head
        this = head.next
        for i in range(sz - sz%k - 1):
            this.next, this, prev = prev, this.next, this
        head.next = this
        # print()
        # for n in b:
            # print(n.val)
        # print()
        # for n in a:
            # print(n.val)
        # print()
        if(len(a) == len(b)):
            a[-1].next = None
        else:
            a[-2].next = a[-1]
        for i in zip(a,b[1:]):
            i[0].next = i[1]
        return b[0]