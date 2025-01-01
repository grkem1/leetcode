# https://leetcode.com/problems/count-ways-to-build-good-strings


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + max(zero, one))
        dp[0] = 1
        for i in range(high):
            dp[i + zero] += dp[i]
            dp[i + one] += dp[i]
        # print(dp)
        return sum(dp[low : high + 1]) % (10**9 + 7)
