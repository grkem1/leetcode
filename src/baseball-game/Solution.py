# https://leetcode.com/problems/baseball-game

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for op in ops:
            if(op == "C"):
                score.pop()
            elif(op == "D"):
                score.append(2*score[-1])
            elif(op == "+"):
                score.append(score[-1]+score[-2])
            else:
                score.append(int(op))
        # print(score)
        return sum(score)