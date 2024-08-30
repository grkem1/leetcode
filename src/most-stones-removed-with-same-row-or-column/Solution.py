# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # greedy doesn't work, no surprise...
        stones = [tuple(s) for s in stones]
        nb = defaultdict(list)
        for i,s in enumerate(stones):
            for s2 in stones[i+1:]:
                if(s[0] == s2[0] or s[1] == s2[1]):
                    nb[s].append(s2)
                    nb[s2].append(s)
        # print(nb)
        seen = set()
        cluster_count = 0

        def dfs(node):
            nonlocal nb, seen
            for n in nb[node]:
                if(n not in seen):
                    seen.add(n)
                    dfs(n)

        for s in stones:
            if(len(seen) == len(stones)):
                break
            if(s in seen):
                continue
            cluster_count += 1
            seen.add(s)
            dfs(s)

        return len(stones) - cluster_count
