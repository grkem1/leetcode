// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return reduce(lambda x,y:x^y, nums + [k]).bit_count()