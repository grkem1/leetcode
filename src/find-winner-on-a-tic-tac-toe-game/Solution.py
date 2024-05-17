# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game

class Solution:
    def tictactoe(self, moves: [[int]]) -> str:
        rocodi = [0]*8 # rows-columns-diagonals(\,/)
        for m in moves[::2]:
            rocodi[m[0]]+=1
            rocodi[m[1]+3]+=1
            if(m[0]==m[1]):rocodi[6]+=1
            if(m[0]+m[1]==2):rocodi[7]+=1
        for m in moves[1::2]:
            rocodi[m[0]]-=1
            rocodi[m[1]+3]-=1
            if(m[0]==m[1]):rocodi[6]-=1
            if(m[0]+m[1]==2):rocodi[7]-=1
        rs = ""
        if(3 in rocodi):rs="A"
        elif(-3 in rocodi):rs="B"
        else:
            if(len(moves)==9):rs="Draw"
            else:rs="Pending"
        return rs
