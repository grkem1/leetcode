# https://leetcode.com/problems/matrix-diagonal-sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        s = 0
        for i in range(m):
            s += mat[i][i]
            s += mat[i][m-1-i]
        if(m % 2 == 1):
            s -= mat[m//2][m//2]
        return s