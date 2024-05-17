# https://leetcode.com/problems/toeplitz-matrix

class Solution:
    def isToeplitzMatrix(self, matrix: [[int]]) -> bool:
        for r1,r2 in zip(matrix,matrix[1:]):
            if(r1[:-1] != r2[1:]):
                return False
        return True