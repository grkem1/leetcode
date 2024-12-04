# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        inc = {l: chr(ord(l) + 1) for l in string.ascii_lowercase}
        inc["z"] = "a"
        j = 0
        for i, l in enumerate(str1):
            if str2[j] in (l, inc[l]):
                j += 1
                if j == len(str2):
                    return True
        return False
