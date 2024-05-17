# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if(p == 0): return 0
        nums.sort()
        left,right = 0,nums[-1]-nums[0]
        def enoughPairs(max_allowed):
            nonlocal nums,p
            total = 0
            i = 0
            while(i < len(nums)-1):
                if(nums[i+1]-nums[i] <= max_allowed):
                    total += 1
                    if(total >= p):
                        return True
                    i+=1
                i+=1
            return False
        while(left < right):
            mid = (left + right) // 2
            if(enoughPairs(mid)):
                right = mid
            else:
                left = mid + 1
        return right