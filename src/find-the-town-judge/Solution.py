# https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_table = [[False for i in range(N)] for j in range(N)]
        for t in trust:
            trust_table[t[0]-1][t[1]-1] = True
        found = -1
        for person,trusts in enumerate(trust_table):
            no_judge = False
            if(trusts.count(True) > 0): continue
            for other,other_trusts in enumerate(trust_table):
                if other == person: continue
                if other_trusts[person] == False:
                    no_judge = True
                    break
            if(no_judge): continue
            if(found != -1): return -1
            found = person+1
        return found