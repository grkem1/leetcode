// https://leetcode.com/problems/stone-game-iv

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        winning = [False,True,False,True]
        if(n < 4):return winning[n]
        for i in range(4,n+1):
            j = 1
            while(j**2 <= i):
                if(winning[i - j**2] == False):
                    winning.append(True)
                    break
                j+=1
            if(len(winning) != i + 1): # not found True
                winning.append(False)
        # print(winning)
        return winning[-1]