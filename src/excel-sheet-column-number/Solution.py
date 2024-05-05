// https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum( (ord(columnTitle[i]) - ord('A') + 1 )*( 26**(len(columnTitle) - i - 1 ) ) for i in range(len(columnTitle)) )