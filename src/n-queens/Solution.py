# https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # see: https://developers.google.com/optimization/cp/queens
        solutions = []
        init_board = [['.' for i in range(n)] for j in range(n)]
        init_constraint_board = [[False for i in range(n)] for j in range(n)]
        # place starting from top row to bottom
        def place_queen(row, board, constraint_board):
            nonlocal n
            for column, threat in enumerate(constraint_board[row]):
                if(threat == False):
                    if(row == n-1):
                        soln = copy.deepcopy(board)
                        soln[row][column] = 'Q'
                        solutions.append([''.join(r) for r in soln])
                    else:
                        i = 1
                        new_constraint_board = copy.deepcopy(constraint_board)
                        new_board = copy.deepcopy(board)
                        new_board[row][column] = 'Q'
                        while(row + i < len(board)):
                            new_constraint_board[row+i][column] = True
                            if(column + i < n): new_constraint_board[row+i][column+i] = True
                            if(column - i >= 0): new_constraint_board[row+i][column-i] = True
                            i+=1
                        place_queen(row+1,new_board,new_constraint_board)
        place_queen(0,init_board,init_constraint_board)
        return solutions