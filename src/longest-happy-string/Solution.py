# https://leetcode.com/problems/longest-happy-string

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        remaining = [[a,'a'],[b,'b'],[c,'c']]
        remaining.sort(reverse=True)
        result = ""
        while(True):
            index = 0
            if(result[-2:] == 2*remaining[0][1]):
                index = 1
            if(remaining[index][0] == 0):
                return result
            result += remaining[index][1]
            remaining[index][0] -= 1
            remaining.sort(reverse=True)
