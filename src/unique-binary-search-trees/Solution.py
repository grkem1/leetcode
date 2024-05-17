# https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    def numTrees(self, n: int) -> int:
        table = [-1]*20
        table[0],table[1],table[2],table[3]=1,1,2,5
        def rec(val):
            nonlocal table
            if(table[val]!=-1):return table[val]
            rv = 0 
            for i in range(val):
                rv += rec(i)*rec(val-i-1)
            table[val]=rv
            return rv
        return rec(n)