// https://leetcode.com/problems/monotonic-array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        last = nums[0]
        pos = False
        neg = False
        for n in nums[1:]:
            if(n > last):
                pos = True
            elif(n < last):
                neg = True
            if(pos and neg):
                return False
            last = n
        return True