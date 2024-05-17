# https://leetcode.com/problems/k-radius-subarray-averages

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if(k == 0): return nums
        if(2*k >= len(nums)): return [-1]*len(nums)
        avgs = []
        acc = [0] + list(accumulate(nums))
        for i in range(len(nums)):
            if(i < k or i >= len(nums)-k):
                avgs.append(-1)
                continue
            avgs.append( int( (acc[i+1+k]-acc[i-k])/(2*k+1) ) )
        return avgs