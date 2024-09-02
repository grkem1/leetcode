# https://leetcode.com/problems/convert-1d-array-into-2d-array

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if(len(original) != m*n):
            return []
        return [ original[i:i+n] for i in range(0,m*n,n) ]
