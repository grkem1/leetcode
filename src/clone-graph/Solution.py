# https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if(node == None): return None
        m = dict()
        v = set()
        q = deque()
        q.append(node)
        while(len(q) > 0):
            n = q.popleft()
            if(n in v):
                continue
            v.add(n)
            if(n not in m):
                m[n] = Node(n.val)
            for nbor in n.neighbors:
                if(nbor not in m): m[nbor] = Node(nbor.val)
                m[n].neighbors.append(m[nbor])
                q.append(nbor)
        return m[node]