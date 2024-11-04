# https://leetcode.com/problems/string-compression-iii

class Solution:
    def compressedString(self, word: str) -> str:
        last = word[0]
        count = 0
        result = ""
        for l in word+'#':
            if(l == last):
                if(count == 9):
                    count = 1
                    result += '9'+last
                else:
                    count += 1
            else:
                result += str(count)+last
                last = l
                count = 1
        return result
