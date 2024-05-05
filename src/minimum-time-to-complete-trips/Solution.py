// https://leetcode.com/problems/minimum-time-to-complete-trips

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def valid(test_time):
            nonlocal time, totalTrips
            trips = 0
            for t in time:
                trips += test_time // t
                if(trips >= totalTrips): return True
            return False
        left,right = 0,max(time)*totalTrips
        while(left < right):
            mid = (left + right) // 2
            if(valid(mid)):
                right = mid
            else:
                left = mid + 1
        return left