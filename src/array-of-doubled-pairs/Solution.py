# https://leetcode.com/problems/array-of-doubled-pairs

class Solution:
    def canReorderDoubled(self, arr: [int]) -> bool:
        c = collections.Counter(sorted(arr,key=lambda i:abs(i)))
        for el in c:
            if(c[el]!=0):
                if(2*el in c):
                    if(c[2*el]>=c[el]):
                        c[2*el]-=c[el]
                    else:
                        return False
                else:
                    return False
        return True