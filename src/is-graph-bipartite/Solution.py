// https://leetcode.com/problems/is-graph-bipartite

class Solution:
    def isBipartite(self, graph: [[int]]) -> bool:
        first = 0
        while(True):
            if(first >= len(graph)): return True
            while(len(graph[first]) == 0):
                first += 1
                if(first >= len(graph)): return True
            s1 = {first}
            s2 = set()
            total_len = 0
            while(total_len != len(s1) + len(s2)):
                total_len = len(s1) + len(s2)
                for i in s1:
                    first = max(first,i)
                    for j in graph[i]:
                        if(j in s1):
                            return False
                        else:
                            s2.add(j)
                for j in s2:
                    first = max(first,j)
                    for i in graph[j]:
                        if(i in s2):
                            return False
                        else:
                            s1.add(i)
                # ~ print(s1)
                # ~ print(s2)
            first += 1
        return True