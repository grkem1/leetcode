// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        total = 0
        if(arr != sorted(arr)):
            arr = sorted(arr)
            total += 1
        if(arr[0] != 1):
            total += 1
        last = 1
        for el in arr[1:]:
            if(el - last > 1):
                total += 1
                last = last + 1
            else:
                last = el
        return last