// https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        i = 2
        lgcd = 1
        while(i <= l1 and i <= l2):
            if(l1 % i == l2 % i == 0):
                l1 //= i
                l2 //= i
                lgcd *= i
            else:
                i += 1
        gcd = str1[:lgcd]
        if( str1 == (len(str1)//lgcd)*gcd and str2 == (len(str2)//lgcd)*gcd ):
            return gcd
        else:
            return ""
