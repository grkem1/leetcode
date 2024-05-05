// https://leetcode.com/problems/count-number-of-homogenous-substrings

class Solution:
    def countHomogenous(self, s: str) -> int:
        last = '#'
        length = 0
        total = 0
        for l in s:
            if(l == last):
                length += 1
            else:
                total += length * (length + 1) // 2
                length = 1
            last = l
        total += length * (length + 1) // 2
        return total % (10**9+7)