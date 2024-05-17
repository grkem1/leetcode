# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d_to_l = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        def dfs(digs):
            nonlocal d_to_l
            if(len(digs)==0): return []
            if(len(digs)==1): return d_to_l[int(digs[0])-2]
            ret = []
            for comb in dfs(digs[:-1]):
                for l in d_to_l[int(digs[-1])-2]:
                    ret.append(comb+l)
            return ret
        return  dfs(digits)