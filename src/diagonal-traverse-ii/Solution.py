# https://leetcode.com/problems/diagonal-traverse-ii

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = []
        for i,row in enumerate(nums):
            for j,el in enumerate(row):
                while(len(diag) < i + j + 1):
                    diag.append([])
                diag[i+j].append(el)
        # print(diag)
        return [el for row in diag for el in row[::-1]]