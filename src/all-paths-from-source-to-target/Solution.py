# https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        pathes = []
        path = []
        def dfs(i):
            nonlocal path,pathes,graph
            dest = len(graph) - 1
            path.append(i)
            if(i == dest):
                pathes.append(path.copy())
                path.pop()
                return
            for j in graph[i]:
                dfs(j)
            path.pop()
        dfs(0)
        return pathes