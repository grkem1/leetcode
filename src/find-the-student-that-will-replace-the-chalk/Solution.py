# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        for i,c in enumerate(chalk):
            if(k < c):
                return i
            k -= c
