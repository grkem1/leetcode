# https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [(n+1)*[0] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + (text1[i-1]==text2[j-1]) )
        return dp[-1][-1]