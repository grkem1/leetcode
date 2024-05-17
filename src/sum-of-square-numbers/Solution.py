# https://leetcode.com/problems/sum-of-square-numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = []
        for i in range(1+math.floor(c**0.5)):
            squares.append(i**2)
        # print(squares)
        i,j=0,len(squares)-1
        while(j>=i):
            s = squares[i]+squares[j]
            if(s > c): 
                j-=1
            elif(s < c): 
                i+=1
            else:
                # print(squares[i],squares[j])
                return True
        return False