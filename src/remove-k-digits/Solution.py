# https://leetcode.com/problems/remove-k-digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        new_num = []
        for n in num:
            while(k > 0 and len(new_num)>0 and n < new_num[-1]):
                k -= 1
                new_num.pop()
            new_num.append(n)
        while(k > 0):
            new_num.pop()
            k -= 1
        i = 0
        while(i < len(new_num) and new_num[i] == '0'):
            i+=1
        if(i == len(new_num)):
            return "0"
        else:
            return "".join(new_num[i:])