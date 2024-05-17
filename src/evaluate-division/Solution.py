# https://leetcode.com/problems/evaluate-division

class Solution:
    def calcEquation(self, equations: [[str]], values: [float], queries: [[str]]) -> [float]:
        transition = collections.defaultdict(dict)
        for i,eq in enumerate(equations):
            transition[eq[0]][eq[1]] = values[i]
            transition[eq[1]][eq[0]] = values[i]**-1
        seen = set()
        def dfs(query,cost = 1.0):
            nonlocal seen
            if(query[0] not in transition): return -1.0
            if(query[0] == query[1]): return 1.0
            if(query[1] in transition[query[0]]) : return transition[query[0]][query[1]]
            seen.add(query[0])
            for hop in transition[query[0]]:
                # ~ print(hop)
                if(hop in seen): continue
                seen.add(hop)
                dist = dfs([hop,query[1]])
                seen.discard(hop)
                if(dist != -1.0):
                    dist *= transition[query[0]][hop]
                    transition[query[0]][query[1]] = dist
                    transition[query[1]][query[0]] = dist**-1
                    seen.discard(query[0])
                    return dist
            seen.discard(query[0])
            return -1.0
        results = []
        for q in queries:
            dist = dfs(q)
            results.append(dist)
        return results