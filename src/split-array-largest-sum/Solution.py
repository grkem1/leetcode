# https://leetcode.com/problems/split-array-largest-sum

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # i = max(nums) # best_possible
        # j = sum(nums) # worst_possible (achievable)
        i = j = 0
        for n in nums:
            i = max(i,n)
            j += n
        def is_achievable(s):
            nonlocal nums,m
            current_splits = 1
            current_sum = 0
            for n in nums:
                current_sum += n
                if(current_sum > s):
                    current_sum = n
                    current_splits += 1
                    if(current_splits > m):
                        return False
            return True
        while(i < j):
            mid = (i + j) // 2
            if(is_achievable(mid)):
                j = mid
            else:
                i = mid + 1
        return j