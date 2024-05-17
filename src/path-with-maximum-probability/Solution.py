# https://leetcode.com/problems/path-with-maximum-probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        m = [[] for i in range(n)]
        for i,e in enumerate(edges):
            m[e[0]].append((e[1],succProb[i]))
            m[e[1]].append((e[0],succProb[i]))
        p = [0]*n
        p[start] = 1
        q = [(-1,start)]
        seen = set()
        while(len(q) > 0 and len(seen) < n and (end not in seen)):
            d,v = heapq.heappop(q)
            if(v in seen): continue
            seen.add(v)
            d = -d
            for nb in m[v]:
                if(nb[1]*d > p[nb[0]]):
                    p[nb[0]] = nb[1]*d
                    heapq.heappush(q,(-p[nb[0]],nb[0]))
        # print(p)
        return p[end]