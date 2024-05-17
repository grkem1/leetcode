# https://leetcode.com/problems/global-and-local-inversions

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        if(A[0] not in (0,1)):return False
        if(A[-1] not in (len(A)-2,len(A)-1)): return False
        for i in range(1,len(A)-1):
            if(A[i] not in (i-1,i,i+1)):
                return False
        return True