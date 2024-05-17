# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left  = [0]
        max_right = [0]
        best_left = 0
        best_right = 0
        for i in range(len(height)):
            best_left = max(best_left, height[i])
            max_left.append(best_left)
            best_right = max(best_right, height[-i-1])
            max_right.append(best_right)
        max_left.append(max_left[-1])
        max_right.append(max_right[-1])
        total = 0
        for i in range(len(height)):
            total += max(0, min(max_left[i],max_right[-i-2]) - height[i])
        return total