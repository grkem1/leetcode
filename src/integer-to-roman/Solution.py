# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        I,V,X,L,C,D,M = 7*[0]
        r_str = ""
        M = num // 1000
        r_str = r_str + M*"M"
        num = num % 1000
        C = num // 100
        if(C == 4):
            r_str = r_str + "CD"
        elif(C == 9):
            r_str = r_str + "CM"
        else:
            r_str = r_str + (C // 5)*"D" + (C % 5)*"C"
        num = num % 100
        X = num // 10
        if(X == 9):
            r_str = r_str + "XC"
        elif(X == 4):
            r_str = r_str + "XL"
        else:
            r_str = r_str + (X // 5)*"L" + (X % 5)*"X"
        num = num % 10
        if(num == 9):
            return r_str + "IX"
        elif(num == 4):
            return r_str + "IV"
        else:
            return r_str + (num // 5)*"V" + (num%5) * "I"

        return r_str
