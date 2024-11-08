# https://leetcode.com/problems/find-if-array-can-be-sorted

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count(n):
            return n .bit_count()
        result = []
        i = 0
        current_max = 0
        while(i < len(nums)):
            this_count = count(nums[i])
            j = i
            while(j < len(nums) and count(nums[j]) == this_count):
                j += 1
            result += sorted(nums[i:j])
            if(result[-j+i] < current_max):
                return False
            current_max = result[-1]
            i = j
        return True
