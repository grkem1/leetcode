// https://leetcode.com/problems/range-addition-ii

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for el in ops:
            m = min(el[0],m)
            n = min(el[1],n)
        return m*n 