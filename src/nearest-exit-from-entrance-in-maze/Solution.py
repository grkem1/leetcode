// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        def isExit(c):
            nonlocal m,n
            return c[0] in (0,m-1) or c[1] in (0,n-1)
        def isValid(c):
            nonlocal m,n,maze
            return -1 < c[0] < m and -1 < c[1] < n and maze[c[0]][c[1]] == '.'
        step = 0
        seen = set()
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        q = collections.deque([tuple(entrance),None])
        while(len(q) > 1):
            c = q.popleft()
            if(c == None):
                step += 1
                q.append(None)
                continue
            if(c in seen):
                continue
            if(isExit(c) and step != 0):
                return step
            for d in directions:
                new_c = (c[0]+d[0],c[1]+d[1])
                if(isValid(new_c)):
                    q.append(new_c)
            seen.add(c)
        return -1