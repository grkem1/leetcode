# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        acc = 0
        for i in range(k):
            acc += nums[i]
        sa_sum = [acc]
        for i in range(k, len(nums)):
            acc += nums[i]
            acc -= nums[i - k]
            sa_sum.append(acc)
        # print(sa_sum)
        dp = [[[0, [0]] for i in range(len(sa_sum))] for _ in range(3)]
        dp[0][0] = [sa_sum[0], [0]]
        for i in range(1, len(sa_sum)):
            dp[0][i] = [sa_sum[i], [i]]
            if dp[0][i][0] <= dp[0][i - 1][0]:
                dp[0][i] = dp[0][i - 1]
            if i >= k:
                dp[1][i] = [sa_sum[i] + dp[0][i - k][0], dp[0][i - k][1] + [i]]
                if dp[1][i - 1][0] >= dp[1][i][0]:
                    dp[1][i] = dp[1][i - 1]
            if i >= 2 * k:
                dp[2][i] = [sa_sum[i] + dp[1][i - k][0], dp[1][i - k][1] + [i]]
                if dp[2][i - 1][0] >= dp[2][i][0]:
                    dp[2][i] = dp[2][i - 1]
        # print(dp[0])
        # print(dp[1])
        # print(dp[2])
        return dp[2][-1][1]
