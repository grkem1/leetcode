// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # return min(zip(r[-1] for r in roads))[0]
        roots = list(range(n))
        def root(a):
            nonlocal roots
            while(roots[a] != a):
                a = roots[a]
            return a
        def connect(a,b):
            nonlocal roots
            r_a,r_b = root(a),root(b)
            roots[r_a] = roots[r_b] = min(r_a,r_b)
        for r in roads:
            connect(r[0]-1,r[1]-1)
        best = 10**4
        for r in roads:
            if(root(r[0]-1) == 0):
                best = min(best, r[-1])
        return best