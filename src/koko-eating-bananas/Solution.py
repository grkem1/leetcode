# https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
#        piles.sort()
#        def satisfies_2(index):
#            nonlocal piles,h
#            return sum((math.ceil(i/piles[index]) for i in piles[index+1:])) + index + 1 <= h
        def satisfies(hour):
            return sum((math.ceil(i/hour)) for i in piles) <= h
        i,j = 1,max(piles)
#        for i in range(1,j+1):
#            if(satisfies(i)):
#                return i
        if(satisfies(1)):return 1
        while(i < j - 1):
            mid = (i + j) // 2
            if(satisfies(mid)):
                j = mid
            else:
                i = mid
        return j