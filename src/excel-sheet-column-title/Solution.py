// https://leetcode.com/problems/excel-sheet-column-title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnTitle = []
        while(columnNumber):
            columnNumber -= 1
            columnNumber,letter = divmod(columnNumber,26)
            columnTitle.append(chr(ord('A')+letter))
        return "".join(columnTitle[::-1])