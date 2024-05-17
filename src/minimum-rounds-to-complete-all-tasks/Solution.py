# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = collections.Counter(tasks)
        total = 0
        for t in c:
            if(c[t] == 1): return -1
            d,m = divmod(c[t],3)
            total += d
            total += (m>0)
        return total