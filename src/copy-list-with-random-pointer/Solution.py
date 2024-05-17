# https://leetcode.com/problems/copy-list-with-random-pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head == None): return None
        dummy = Node(0)
        orig = head
        copy = dummy
        orig_clone = dict()
        while(orig):
            copy.next = Node(orig.val)
            orig_clone[orig] = copy.next
            orig,copy = orig.next,copy.next
        original = head
        clone = dummy.next
        while(original):
            if(original.random):
                clone.random = orig_clone[original.random]
            original = original.next
            clone = clone.next
        return dummy.next