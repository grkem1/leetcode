// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        for j in range(m//2):
            for i in range(j,m-1-j):
                matrix[j][i], matrix[i][m-1-j], matrix[m-1-j][m-1-i], matrix[m-1-i][j] = matrix[m-1-i][j], matrix[j][i], matrix[i][m-1-j], matrix[m-1-j][m-1-i]
        # print(matrix)