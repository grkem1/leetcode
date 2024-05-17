# https://leetcode.com/problems/maximum-performance-of-a-team

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eff_speed = sorted(zip(efficiency,speed),reverse=True)
        sum_speeds = 0
        max_perf = 0
        for i in range(k):
            sum_speeds += eff_speed[i][1]
            max_perf = max_perf = max(sum_speeds * eff_speed[i][0],max_perf)
        if(n == k): return (max_perf% (10**9 + 7))
        max_speeds = [s for eff,s in eff_speed[:k]]
        heapq.heapify(max_speeds)
        for i in range(k,n):
            if(eff_speed[i][1] > max_speeds[0]):
                sum_speeds += (eff_speed[i][1] - max_speeds[0])
                heapq.heapreplace(max_speeds,eff_speed[i][1])
                max_perf = max(max_perf,sum_speeds*eff_speed[i][0])
        return (max_perf%(10**9+7))
