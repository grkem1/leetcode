// https://leetcode.com/problems/shortest-path-visiting-all-nodes

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        ending_mask = 2**N-1
        dp = dict()
        def dfs(node_index,state):
            nonlocal N,ending_mask,dp,graph
            neighbors = graph[node_index]
            if( (state | (1 << node_index)) == ending_mask):
                return 0
            if( (node_index,state) in dp ):
                return dp[ (node_index,state) ]
            dp[ (node_index,state) ] = 2**10
            best = 2**10
            for neighbor in neighbors:
                best = min(best, 1 + min( dfs(neighbor,state | (1 << node_index)), dfs(neighbor,state)) )
            dp[ (node_index,state) ] = best
            return best
        best = 2**10
        for node_index,neighbors in enumerate(graph):
            best = min(best,dfs(node_index,0))
        return best