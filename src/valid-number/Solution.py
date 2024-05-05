// https://leetcode.com/problems/valid-number

class Solution:
    def isNumber(self, s: str) -> bool:
        constituents = re.split('e|E',s)
        if(len(constituents) > 2): return False
        number = constituents[0]
        if(len(constituents) == 2): exponent = constituents[1]
        else:            exponent = None
        if(len(number) == 0): return False
        if(number[0] in ('+','-')):
            number = number[1:]
            if(len(number) == 0): return False
        if(number == '.'): return False
        dot = False
        for char in number:
            if(char.isdecimal()): continue
            if(char == '.'):
                if(dot == True): return False
                else:
                    dot = True
            else:
                return False
        if(exponent != None):
            if(len(exponent) == 0): return False
            if(exponent[0] in ('+','-')):
                exponent = exponent[1:]
                if(len(exponent) == 0): return False
            return exponent.isdecimal()
        return True
