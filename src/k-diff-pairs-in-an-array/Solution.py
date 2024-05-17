# https://leetcode.com/problems/k-diff-pairs-in-an-array

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        found = collections.Counter(nums)
        count = 0
        if(k == 0):
            for n in found:
                count += [0,1][found[n]>1]
        else:
            for n in found:
                if( (n+k) in found):
                    count += 1
        return count