# https://leetcode.com/problems/sum-of-subarray-minimums

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        s = [(-2**15,-1)]
        for i,el in enumerate(arr):
            while(len(s) > 1 and el < s[-1][0]):
                l1 = i - s[-1][1]
                l2 = s[-1][1] - s[-2][1]
                res += s[-1][0]* l1 * l2
                s.pop()
            s.append((el,i))
        while(len(s) > 1):
            el,i = s.pop()
            l1 = len(arr)-i
            l2 = i - s[-1][1]
            res += el * l1 * l2
        return res % (10**9+7)