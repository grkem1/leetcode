# https://leetcode.com/problems/minimum-cost-for-tickets


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [10**9] * (days[-1] + 1)
        dp[0] = 0
        days_set = set(days)
        for i in range(1, len(dp)):
            if i in days_set:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2],
                )
            else:
                dp[i] = dp[i - 1]
        # print(dp)
        return dp[-1]
