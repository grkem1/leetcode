// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def simulate(capacity):
            nonlocal weights,days
            b = 0
            d = 1
            for w in weights:
                if(b + w <= capacity):
                    b += w
                else:
                    b = w
                    d += 1
                    if(d > days):return False
            return True
        left = max(weights)  # lower boundary
        right = sum(weights) # upper boundary
        if(simulate(left)): return left
        while(left + 1 < right):
            mid = (left + right) // 2
            if(simulate(mid)):
                right = mid
            else:
                left = mid
        return right