// https://leetcode.com/problems/minimum-speed-to-arrive-on-time

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if(hour <= len(dist)-1):
            return -1
        longest = max(dist)
        def onTime(speed):
            nonlocal dist,hour
            if(speed == 0): return False
            time = 0
            for d in dist[:-1]:
                time += ceil(d/speed)
                if(time >= hour):
                    return False
            time += dist[-1]/speed
            return time <= hour
        left,right = 0,longest
        if(hour - int(hour) != 0):
            right = max(right, ceil(dist[-1]/(hour - int(hour))))
        # print(right)
        # if(dist[-1]!=int(dist[-1])):print(ceil(dist[-1]/(dist[-1]-int(dist[-1]))))
        while(left < right-1):
            mid = (left + right) // 2
            if(onTime(mid)):
                right = mid
            else:
                left = mid
        return right