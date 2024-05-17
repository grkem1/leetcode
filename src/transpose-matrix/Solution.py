# https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        new_matrix = [[0]*m for k in range(n)]
        for i,row in enumerate(matrix):
            for j,el in enumerate(row):
                new_matrix[j][i] = el
        return new_matrix