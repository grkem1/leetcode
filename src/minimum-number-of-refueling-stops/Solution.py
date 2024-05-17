# https://leetcode.com/problems/minimum-number-of-refueling-stops

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxFuels = []
        current = [0,startFuel]
        visited = 0
        stations.append([target,0])
        for s in stations:
            # ~ print(current)
            current[1] -= s[0] - current[0]
            current[0] = s[0]
            if(current[1] < 0):
                if(len(maxFuels) == 0): return -1
                while(current[1] < 0 and len(maxFuels) > 0): 
                    current[1] -= heapq.heappop(maxFuels)
                    visited += 1
                if(current[1] < 0): return -1
            heapq.heappush(maxFuels, -s[1])
        return visited