# https://leetcode.com/problems/swapping-nodes-in-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        nodes = []
        while(head):
            nodes.append(head)
            head = head.next
        nodes[k-1].val,nodes[-k].val = nodes[-k].val,nodes[k-1].val
        return nodes[0]