# https:#leetcode.com/problems/k-th-smallest-prime-fraction

import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = [(arr[i]/arr[-1],i,len(arr)-1) for i in range(len(arr)-1)]
        fractions.append( (arr[-1]/arr[-2],len(arr)-1, len(arr)-2) )
        for _ in range(k-1):
            # print(fractions)
            new_divisor_index = fractions[0][-1] - 1
            dividend_index    = fractions[0][-2]
            if(new_divisor_index == dividend_index):
                new_divisor_index -= 1
            if(new_divisor_index < 0):
                heapq.heappop(fractions)
            else:
                dividend = arr[dividend_index]
                divisor  = arr[new_divisor_index]
                heapq.heapreplace(fractions, (dividend/divisor, dividend_index, new_divisor_index) )
        return [arr[fractions[0][1]], arr[fractions[0][2]]]
