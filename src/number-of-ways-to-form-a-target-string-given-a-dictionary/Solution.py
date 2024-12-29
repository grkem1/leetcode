# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        frequencies = [defaultdict(int) for _ in range(len(words[0]))]
        for i, w in enumerate(words):
            for j, l in enumerate(w):
                frequencies[j][l] += 1
        dp = [[0] * len(frequencies) for _ in range(len(target))]
        dp[0][0] = frequencies[0][target[0]]
        for i in range(1, len(frequencies)):
            dp[0][i] = frequencies[i][target[0]] + dp[0][i - 1]
        for i in range(1, len(target)):
            for j in range(i, len(frequencies)):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] * frequencies[j][target[i]]
        # for r in dp:
        #     print(r)
        return dp[-1][-1] % (10**9 + 7)
