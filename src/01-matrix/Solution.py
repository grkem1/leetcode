# https://leetcode.com/problems/01-matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        q = deque()
        seen = set()
        for i in range(m):
            for j in range(n):
                if(mat[i][j] == 1):
                    if(i < m-1 and mat[i+1][j] == 0 or i > 0 and mat[i-1][j] == 0 or j < n-1 and mat[i][j+1] == 0 or j > 0 and mat[i][j-1] == 0):
                        q.append((i,j))
                        seen.add((i,j))
                    # else: mat[i][j] = 10**4
        q.append(None)
        level = 1
        while(len(q) > 1):
            index = q.popleft()
            if(not index):
                # print(mat)
                q.append(index)
                level += 1
                # print(q)
                continue
            i,j = index
            # print(i,j,level)
            mat[i][j] = level
            for k in (-1,1):
                if(0 <= i+k < m and ((i+k,j) not in seen) and mat[i+k][j] != 0):
                    q.append((i+k,j))
                    seen.add((i+k,j))
                if(0 <= j+k < n and (i,j+k) not in seen and mat[i][j+k] != 0):
                    q.append((i,j+k))
                    seen.add((i,j+k))
        return mat