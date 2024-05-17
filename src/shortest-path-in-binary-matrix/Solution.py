# https://leetcode.com/problems/shortest-path-in-binary-matrix

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        # if(grid[0][0] != 0):
        #     if(m == 1):
        #         return 1
        #     else:
        #         return -1
        def neighbors(cell):
            nonlocal m,n
            x = [-1,0,1] if cell[1] > 0 else [0,1]
            y = [-1,0,1] if cell[0] > 0 else [0,1]
            if(cell[1] == n-1):
                x.pop()
            if(cell[0] == m-1):
                y.pop()
            for x_ in x:
                for y_ in y:
                    if(x == y == 0):
                        continue
                    yield (cell[0]+y_,cell[1]+x_)

        q_start = collections.deque()
        q_end = collections.deque()
        visited_start = set()
        # visited_start.add((0,0))
        visited_end = set()
        # visited_end.add((m-1,n-1))
        if(grid[0][0] == 0):q_start.append((0,0))
        if(grid[-1][-1] == 0):q_end.append((m-1,n-1))
        level = 0
        while(len(q_start) > 0 and len(q_end) > 0):
            # print("q_start:", q_start)
            # print("q_end:", q_end)
            new_q_start = collections.deque()
            while(len(q_start) > 0):
                cell = q_start.popleft()
                if(cell in visited_start):
                    continue
                if(cell in visited_end):
                    return level
                visited_start.add(cell)
                for neighbor in neighbors(cell):
                    if(neighbor not in visited_start and grid[neighbor[0]][neighbor[1]] == 0):
                        new_q_start.append(neighbor)
            q_start = new_q_start
            level += 1
            new_q_end = collections.deque()
            while(len(q_end) > 0):
                cell = q_end.popleft()
                if(cell in visited_end):
                    continue
                if(cell in visited_start):
                    return level
                visited_end.add(cell)
                for neighbor in neighbors(cell):
                    if(neighbor not in visited_end and grid[neighbor[0]][neighbor[1]] == 0):
                        new_q_end.append(neighbor)
            level += 1
            q_end = new_q_end
            # print("new_q_start:", new_q_start)
            # print("new_q_end:", new_q_end)
        return -1