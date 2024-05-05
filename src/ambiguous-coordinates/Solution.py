// https://leetcode.com/problems/ambiguous-coordinates

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def generator(s:str):
            if(len(s) == 0): return []
            if(len(s) == 1): return [s]
            dot = no_dot = True
            if(s[-1] == '0'):
                if(s[0] == '0'):
                    return []
                else:
                    return[s]
            if(s[0] == '0'): # and s[-1] != 0
                return [ '0.' + s[1:] ]
            return [s] + [s[:i] + '.' + s[i:] for i in range(1,len(s))]
        stripped = s[1:-1]
        rl = []
        for comma in range(1, len(stripped)):
            rl += ['(' + i[0] + ', ' + i[1] + ')' for i in  itertools.product(generator(stripped[:comma]),generator(stripped[comma:]))]
        return rl