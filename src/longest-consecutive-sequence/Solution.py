// https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        c = collections.Counter(nums)
        best = 0 
        while(len(c) > 0): 
            el,_ = c.popitem()
            i = 1 
            while(el+i in c): 
                c.pop(el+i)
                i+=1
            j = 1 
            while(el-j in c): 
                c.pop(el-j)
                j+=1
            best = max(best,i+j-1)
        return best