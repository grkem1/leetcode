# https://leetcode.com/problems/maximum-matrix-sum

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        lowest = 10**6
        total = -2*lowest
        even = True
        zero = False
        for r in matrix:
            for el in r:
                if(el == 0):
                    zero = True
                if(el < 0):
                    even = not even
                if(abs(el) < lowest):
                    total += 2*lowest
                    lowest = abs(el)
                    total -= lowest
                else:
                    total += abs(el)
        if(even or zero):
            total += 2*lowest
        return total
