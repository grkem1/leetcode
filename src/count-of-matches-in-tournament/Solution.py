# https://leetcode.com/problems/count-of-matches-in-tournament

class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while(n > 1):
            n,rem = divmod(n,2)
            total += n
            n += rem
        return total