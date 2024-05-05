// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        remaining = k - n
        if(remaining == 0):return "a"*n
        z_count, transition = divmod(remaining,25)
        if(transition == 0):
            transition_str = ""
        else:
            transition_str = chr(ord('a')+transition)
        return "a"*(n-z_count-(transition>0) )+ transition_str +"z"*z_count