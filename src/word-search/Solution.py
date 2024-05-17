# https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        prevs = []
        def search(index,row,column):
            nonlocal word,prevs,board
            #print(prevs)
            if(index==len(word)):return True
            if(row < 0 or column < 0 or row >= len(board) or column >= len(board[0])): return False
            if(board[row][column]==word[index] and (row,column) not in prevs):
                prevs+=[(row,column)]
            else:
                return False
            if(search(index+1,row+1,column) or search(index+1,row-1,column) or search(index+1,row,column-1) or search(index+1,row,column+1)):
                return True
            prevs.pop()
            return False
        for row in range(len(board)):
            for column in range(len(board[0])):
                if(search(0,row,column)):
                    return True
        return False
