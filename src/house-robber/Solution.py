// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        last_one, last_two, last_three = 0,0,0
        current = 0
        best = 0
        for n in nums:
            current = max(last_two,last_three)+n
            best = max(best,current)
            last_one, last_two, last_three = current, last_one, last_two
        return best