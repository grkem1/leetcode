# https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if(len(nums) == 0):
            return ranges
        start = nums[0]
        end = nums[0]
        nums.append(nums[0])
        for num in nums[1:]:
            if(num == end+1):
                end = num
            else:
                if(start == end):
                    ranges.append(str(start))
                else:
                    ranges.append(str(start)+"->"+str(end))
                start = end = num
        return(ranges)