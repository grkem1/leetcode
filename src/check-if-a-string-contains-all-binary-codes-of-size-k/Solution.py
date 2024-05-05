// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        includes = [False]*(2**k)
        total = 0
        for i in range(len(s) - k + 1):
            number = int(s[i:i+k],2)
            # print(number)
            # print(includes)
            if(not includes[number]):
                includes[number] = True
                total += 1
                if(total == 2**k):
                    return True
        return False