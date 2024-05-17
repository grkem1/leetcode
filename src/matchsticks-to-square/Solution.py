# https://leetcode.com/problems/matchsticks-to-square

class Solution:
    def makesquare(self, matchsticks: [int]) -> bool:
        matchsticks.sort()
        seen = {} 
        s = sum(matchsticks)
        if(s % 4 != 0):
            return False
        if(any(i > s//4 for i in matchsticks)):
            return False
        remaining = [sum(matchsticks)//4]*4
        def dfs():
            nonlocal matchsticks,remaining,seen
#            print(remaining)
            if(remaining == [0]*4):
                return True 
            if(any(i < 0 for i in remaining)):
                return False
            if(tuple(remaining) in seen):
                return seen[tuple(remaining)]
            val = matchsticks.pop()
            state = False
            remaining[0] -= val
            state |= dfs()
            remaining[0] += val
            if(not state):
                remaining[1] -= val
                state |= dfs()
                remaining[1] += val
            if(not state):
                remaining[2] -= val
                state |= dfs()
                remaining[2] += val
            if(not state):
                remaining[3] -= val
                state |= dfs()
                remaining[3] += val
            matchsticks.append(val)
            for r in itertools.permutations(remaining):
                seen[tuple(r)] = state
            return state
        return dfs()