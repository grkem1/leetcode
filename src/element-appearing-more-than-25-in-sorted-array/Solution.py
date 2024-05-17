# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) // 4
        last = -1
        streak = 1
        for el in arr:
            if(el == last):
                streak += 1
            else:
                last = el
                streak = 1
            if(streak > threshold):
                return el