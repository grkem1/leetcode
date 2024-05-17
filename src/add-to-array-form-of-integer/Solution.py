# https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = num[::-1]
        c = 0
        i = 0
        while(k > 0 or c > 0):
            d = k % 10
            k //= 10
            if(len(s) <= i):
                s.append(0)
            s[i] += c + d
            if(s[i] > 9):
                c = 1
                s[i] -= 10
            else:
                c = 0
            i += 1
        return s[::-1]