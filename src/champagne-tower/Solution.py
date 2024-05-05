// https://leetcode.com/problems/champagne-tower

class Solution:
    def champagneTower(self, poured: float, query_row: int, query_glass: int) -> float:
        cache = collections.defaultdict(float)
        cache[(0,0)] = poured
        def pourChampagne(query_row,query_glass):
            nonlocal cache
            if(query_glass < 0 or query_glass > query_row):
                return 0
            if((query_row,query_glass) in cache):
                return cache[(query_row,query_glass)]
            left = max(0,pourChampagne(query_row-1,query_glass-1)-1)/2
            right = max(0,pourChampagne(query_row-1,query_glass)-1)/2
            cache[(query_row,query_glass)] = left + right
            return left + right
        pourChampagne(query_row,query_glass)
        # print(cache)
        return min(cache[(query_row,query_glass)],1)