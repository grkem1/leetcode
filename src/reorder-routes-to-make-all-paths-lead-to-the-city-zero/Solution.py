// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        total = 0
        adjList = [[] for i in range(n)]
        adjListRev = [[] for i in range(n)]
        for c in connections:
            adjList[c[0]].append(c[1])
            adjListRev[c[1]].append(c[0])
        q = deque([0])
        seen = set()
        while(len(q) > 0):
            o = q.popleft()
            seen.add(o)
            for i in adjListRev[o]:
                if(i not in seen):
                    adjList[o].append(i)
                    total += 1
            for i in adjList[o]:
                if(i not in seen):
                    q.append(i)
            # print(q)
        # print(adjList)
        return n - 1 - total