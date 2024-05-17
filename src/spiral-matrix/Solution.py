# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        solns_array = []
        direction = 0
        while(True):
            if(len(matrix) == 0):
                return solns_array
            if(direction == 0):
                solns_array += matrix[0]
                matrix = matrix[1:]
            elif(direction == 1):
                if(len(matrix[0]) == 1):
                    return solns_array + [i[0] for i in matrix]
                solns_array += [row[-1] for row in matrix]
                matrix = [row[:-1] for row in matrix]
            elif(direction == 2):
                solns_array += matrix[-1][-1::-1]
                matrix = matrix[:-1]
            elif(direction == 3):
                if(len(matrix[0]) == 1):
                    return solns_array + [i[0] for i in matrix][-1::-1]
                solns_array += [row[0] for row in matrix][-1::-1]
                matrix = [row[1:] for row in matrix]
            direction = (direction + 1) % 4