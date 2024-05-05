// https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        l=0
        for n in nums:
            if(n==1):
                l+=1
                m = max(m,l)
            else:
                l=0
        return m