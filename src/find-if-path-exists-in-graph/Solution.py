# https://leetcode.com/problems/find-if-path-exists-in-graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        m = [[] for i in range(n)]
        for e in edges:
            m[e[0]].append(e[1])
            m[e[1]].append(e[0])
        seen = set()
        q = deque([source])
        while(destination not in seen and len(q) > 0 and len(seen) < n):
            current = q.popleft()
            if(current in seen): continue
            seen.add(current)
            for nbor in m[current]:
                q.append(nbor)
        return destination in seen