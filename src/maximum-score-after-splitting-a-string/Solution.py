# https://leetcode.com/problems/maximum-score-after-splitting-a-string


class Solution:
    def maxScore(self, s: str) -> int:
        total = sum(int(l) for l in s)
        best = 0
        for l in s[:-1]:
            total += 2 * (l == "0") - 1
            best = max(best, total)
        return best
