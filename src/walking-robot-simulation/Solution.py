# https://leetcode.com/problems/walking-robot-simulation

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def dist(p):
            return p[0] ** 2 + p[1] ** 2

        o_map = set(tuple(i) for i in obstacles)

        furthest = 0
        dir = deque([[0,1],[1,0],[0,-1],[-1,0]])
        pos = [0,0]
        for c in commands:
            if(c == -1):
                dir.rotate(-1)
                continue
            if(c == -2):
                dir.rotate()
                continue
            for _ in range(c):
                pos[0] += dir[0][0]
                pos[1] += dir[0][1]
                if(tuple(pos) in o_map):
                    pos[0] -= dir[0][0]
                    pos[1] -= dir[0][1]
                    break
            # print(pos)
            furthest = max(furthest, dist(pos))

        return furthest
