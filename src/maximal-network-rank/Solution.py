// https://leetcode.com/problems/maximal-network-rank

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for r in roads:
            adj[r[0]].append(r[1])
            adj[r[1]].append(r[0])
        best = 0
        for i in range(len(adj)):
            for j in range(i+1,len(adj)):
                best = max(best, len(adj[i])+len(adj[j])-(j in adj[i]))
        return best