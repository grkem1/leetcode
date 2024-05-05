// https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3]) - target
        for i,first in enumerate(nums):
            # print(nums, closest)
            j=i+1;k=len(nums)-1
            while(k > j):
                s = first + nums[k] + nums[j] - target
                if(s == 0):
                    return target
                elif(s > 0):
                    k -= 1
                else:
                    j += 1
                if(abs(s) < abs(closest)): closest = s
            if(sum(nums[i:i+3]) > target): break # it will only get worse
        return target + closest