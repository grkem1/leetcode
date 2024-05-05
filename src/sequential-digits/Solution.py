// https://leetcode.com/problems/sequential-digits

class Solution:
    def sequentialDigits(self, low: int, high: int) -> [int]:
        digits = "123456789"
        between = []
        for l in range(int(math.log10(low)), int(math.log10(high))+1):
            # print(l)
            for offset in range(0, 9-l):
                number = int(digits[offset:offset+l+1])
                if(number < low):
                    continue
                elif(number > high):
                    break
                between.append(number)
        return between