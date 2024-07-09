# https://leetcode.com/problems/average-waiting-time

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cumulative_waiting_time = 0
        time = 0
        for c in customers:
            if c[0] > time:
                time = c[0]
            time += c[1]
            cumulative_waiting_time += time - c[0]
        return cumulative_waiting_time / len(customers)
