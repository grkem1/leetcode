# https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = [0]*5 # b-a-l-o-n
        for l in text:
            if(l == 'b'):letters[0]+=1
            elif(l == 'a'):letters[1]+=1
            elif(l == 'l'):letters[2]+=1
            elif(l == 'o'):letters[3]+=1
            elif(l == 'n'):letters[4]+=1
        letters[2]//=2
        letters[3]//=2
        return min(letters)