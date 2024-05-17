# https://leetcode.com/problems/game-of-life

class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        m,n = len(board),len(board[0])
        def get_cell(i,j):
            nonlocal board
            if(i < 0 or i >= m or j < 0 or j >= n):
                return 0
            return board[i][j]

        def live_neighbor_count(i,j):
            count = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    count += get_cell(i+k,j+l)
            return count - board[i][j]

        toggle = [] # find all cells to be toggled
        for row_index,row in enumerate(board):
            for column_index,cell in enumerate(row):
                count = live_neighbor_count(row_index,column_index)
                if(cell == 1 and count not in (2,3) or cell == 0 and count == 3):
                    toggle.append((row_index,column_index))

        for (i,j) in toggle:
            board[i][j] = 1 - board[i][j]