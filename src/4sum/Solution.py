# https://leetcode.com/problems/4sum

class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        foursomes = []
        for a in range(len(nums)-3):
            for b in range(a+1,len(nums)-2):
                c = b+1
                d = len(nums)-1
                this_target = target - nums[a] - nums[b]
                while(d > c):
                    current = nums[d] + nums[c]
                    if(this_target == current):
                        if([nums[a],nums[b],nums[c],nums[d]] not in foursomes):
                            foursomes.append([nums[a],nums[b],nums[c],nums[d]])
                        d = d - 1
                        while(nums[d] == nums[d+1] and d >= 0):
                            d = d - 1
                        c = c + 1
                        while(nums[c] == nums[c-1] and c <= d):
                            c = c + 1
                    elif(this_target > current):
                        c = c + 1
                    else:
                        d = d - 1
        return foursomes

