// https://leetcode.com/problems/eliminate-maximum-number-of-monsters

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_to_reach = []
        for i,d in enumerate(dist):
            time_to_reach.append(ceil(d/speed[i]))
        time_to_reach.sort()
        time = 0
        while(time < len(dist) and time < time_to_reach[time]):
            time += 1
        return time