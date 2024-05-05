// https://leetcode.com/problems/super-palindromes

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def inc(char):
            return str(int(char)+1)
        def findnextpalindrome(s):
            l = len(s)
            for i in range(l//2,l):
                if(s[i] == '9'):continue
                j = l - i - 1
                if(i == j): return s[:l//2]+inc(s[l//2])+s[l//2+1:]
                nc = inc(s[i])
                return s[:j] + nc + (i-j-1)*'0' + nc + s[i+1:]
            return '1' + (l-1)*'0' + '1'

        def ispalindrome(p):
            # original = p
            digit_count = math.floor(math.log10(p))+1
            reverse = 0
            for i in range(digit_count//2):
                reverse *= 10
                reverse += p % 10
                p //= 10
            if(digit_count % 2 == 1): p //= 10 # throw away the middle digit
            # if(reverse == p): print(original)
            return (reverse == p)
        sqrt_left = math.ceil(math.sqrt(int(left)))
        sqrt_right = str(math.floor(math.sqrt(int(right))))
        if(ispalindrome(sqrt_left) == False):
            temp = str(sqrt_left)
            s_l = temp[::]
            l = len(temp)
            temp = temp[:l//2] + ('' if (l%2 == 0) else temp[l//2] ) + temp[:l//2][::-1]
            while(temp < s_l): temp = findnextpalindrome(temp)
            sqrt_left = temp
        else: sqrt_left = str(sqrt_left)
        count = 0
        while(len(sqrt_right) > len(sqrt_left) or sqrt_left <= sqrt_right):
            if(ispalindrome(int(sqrt_left)**2)):
                # print(sqrt_left)
                count +=1
            sqrt_left = findnextpalindrome(sqrt_left)
        return count