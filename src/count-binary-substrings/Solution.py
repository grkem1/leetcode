# https://leetcode.com/problems/count-binary-substrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last = s[0]
        consecutives = [1]
        for c in s[1:]:
            if c == last: consecutives[-1]+=1
            else: consecutives += [1]
            last = c
        # print(consecutives)
        last_c = consecutives[0]
        count = 0
        for el in consecutives[1:]:
            count += min(last_c,el)
            last_c = el
        return count