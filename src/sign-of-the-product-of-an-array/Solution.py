// https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for el in nums:
            if (el == 0):
                return 0
            if (el < 0):
                sign = -sign
        return sign