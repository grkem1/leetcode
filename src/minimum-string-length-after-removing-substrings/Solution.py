# https://leetcode.com/problems/minimum-string-length-after-removing-substrings

class Solution:
    def minLength(self, s: str) -> int:
        # Greedy works since searched strings have distinct letters
        new_str = []
        for c in s:
            if(len(new_str) > 0 and (c == 'B' and new_str[-1] == 'A' or c == 'D' and new_str[-1] == 'C') ):
                new_str.pop()
            else:
                new_str.append(c)
            # print(new_str)
        return len(new_str)
