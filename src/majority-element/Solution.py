# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common(1)[0][0]