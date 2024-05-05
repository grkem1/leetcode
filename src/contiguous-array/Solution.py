// https://leetcode.com/problems/contiguous-array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = dict([(0,-1)])
        max_array = 0
        current = 0
        for i,n in enumerate(nums):
            current += (2*n-1)
            if(current in first_seen):
                max_array = max(max_array,i-first_seen[current])
            else:
                first_seen[current] = i
            # print(current)
            # print(first_seen)
        return max_array