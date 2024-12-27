# https://leetcode.com/problems/maxScoreSightseeingPair


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_score = 0
        best_left_score = 0
        for v in values:
            best_left_score -= 1
            best_score = max(best_score, best_left_score + v)
            best_left_score = max(best_left_score, v)
        return best_score
