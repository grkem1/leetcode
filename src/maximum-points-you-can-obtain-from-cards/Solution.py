# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints)
        window_length = l - k
        if(window_length == 0): return sum(cardPoints)
        cur_min = moving_sum = sum(cardPoints[0:window_length])
        total_sum = moving_sum + sum(cardPoints[window_length:])
        for shift in range(1,k+1):
            moving_sum += cardPoints[shift + window_length - 1] - cardPoints[shift - 1]
            cur_min = min(cur_min,moving_sum)
        return total_sum - cur_min