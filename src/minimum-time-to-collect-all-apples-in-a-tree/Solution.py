# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        parents = dict()
        edges_dict = defaultdict(list)
        for e in edges:
            edges_dict[e[0]].append(e[1])
            edges_dict[e[1]].append(e[0])
        seen = set()
        seen.add(0)
        q = deque([0])
        while(len(q) > 0):
            n = q.popleft()
            for nb in edges_dict[n]:
                if(nb not in seen):
                    seen.add(nb)
                    q.append(nb)
                    parents[nb] = n
        # print(parents)
        seen = set()
        seen.add(0)
        total = 0
        for n,hA in enumerate(hasApple):
            if(hA == False): continue
            dist = 0
            while(n not in seen):
                seen.add(n)
                n = parents[n]
                dist += 1
            total += 2*dist
        return total