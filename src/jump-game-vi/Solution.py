// https://leetcode.com/problems/jump-game-vi

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        previous = [(-nums[0],-1)]
        res = nums[0]
        for index,n in enumerate(nums[1:]):
            while(index-k>previous[0][1]):
                heapq.heappop(previous)
            res = n - previous[0][0]
            heapq.heappush(previous,(-res,index))
        return res
