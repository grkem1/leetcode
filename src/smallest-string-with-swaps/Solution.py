# https://leetcode.com/problems/smallest-string-with-swaps

class Solution:
    def smallestStringWithSwaps(self,s,pairs) -> str:
        s = [l for l in s]
        groups = [i for i in range(len(s))]
        def find_root(i):
            nonlocal groups
            root = i
            while(groups[root] != root):
                root = groups[root]
            return root
        for p in pairs:
            p1,p2 = p
            r1,r2 = find_root(p1),find_root(p2)
            groups[r1] = groups[r2] = min(r1,r2)
        # ~ print(groups)
        for i in range(len(groups)):
            groups[i] = groups[groups[i]]
        # ~ print(groups)
        group_elements = collections.defaultdict(list)
        for i,g in enumerate(groups):
            group_elements[g].append(i)
        # ~ print(group_elements)
        for indices in group_elements.values():
            # ~ print(s)
            # ~ print(indices)
            for i,l in enumerate(sorted(s[i] for i in indices)):
                s[indices[i]] = l
        return ''.join(s)