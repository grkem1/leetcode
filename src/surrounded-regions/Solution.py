// https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board: [[str]]) -> None:
        not_surrounded = set()
        def dfs(i,j):
            nonlocal board,not_surrounded
            if(i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1):
                #print("here")
                return
            if(board[i][j]!='O' or (i,j) in not_surrounded):
                #print("there")
                return
            not_surrounded.add((i,j))
            for (x,y) in ( (0,1),(1,0),(0,-1),(-1,0) ):
                #print("bonanza")
                dfs(i+x,j+y)
        for i,el in enumerate(board[0]):
            if(el == 'O'):
                dfs(0,i)
        for i,el in enumerate(board[-1]):
            if(el == 'O'):
                dfs(len(board)-1,i)
        for i in range(len(board)):
            if(board[i][0] == 'O'):
                dfs(i,0)
        for i in range(len(board)):
            if(board[i][len(board[0])-1] == 'O'):
                dfs(i,len(board[0])-1)
        for (i,j) in not_surrounded:
            dfs(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if( (i,j) not in not_surrounded ):
                    board[i][j] = 'X'