# https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        zcolumns = set()
        for row_i,row in enumerate(matrix):
            found = False
            for col_i,el in enumerate(row):
                if(el == 0):
                    found = True
                    zcolumns.add(col_i)
                elif(found):
                    matrix[row_i][col_i] = 0
            if(found):
                for i in range(n):
                    if(matrix[row_i][i]!=0):
                        matrix[row_i][i]=0
                    else:break
        for zc in zcolumns:
            for i in range(m):
                matrix[i][zc] = 0
        return