// https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[],[]]
        players_losses = dict()
        for m in matches:
            if(m[1] in players_losses):
                players_losses[m[1]] += 1
            else:
                players_losses[m[1]] = 1
            if(m[0] not in players_losses):
                players_losses[m[0]] = 0
        for p in players_losses:
            if(players_losses[p] == 1):
                answer[1].append(p)
            elif(players_losses[p] == 0):
                answer[0].append(p)
        return [sorted(answer[0]),sorted(answer[1])]