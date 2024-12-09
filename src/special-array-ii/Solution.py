# https://leetcode.com/problems/special-array-ii


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        p = (nums[0] + 1) % 2
        inflection = []
        for i, n in enumerate(nums):
            if n % 2 == p:
                inflection.append(i)
            p = n % 2
        result = []
        # print(inflection)
        for q in queries:
            result.append(
                bisect.bisect(inflection, q[0]) == bisect.bisect(inflection, q[1])
            )
        return result
