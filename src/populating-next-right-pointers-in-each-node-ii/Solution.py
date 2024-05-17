# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if(root == None):return None
        q = collections.deque()
        q.append(root)
        while(len(q) > 0):
            new_q = collections.deque()
            while(len(q) > 1):
                node = q.popleft()
                next_right_node = q[0]
                node.next = next_right_node
                if(node.left):new_q.append(node.left)
                if(node.right):new_q.append(node.right)
            node = q.popleft()
            if(node.left):new_q.append(node.left)
            if(node.right):new_q.append(node.right)
            q = new_q
        return root
        