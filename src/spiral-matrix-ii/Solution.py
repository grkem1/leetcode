# https://leetcode.com/problems/spiral-matrix-ii

class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        # S. Pochmann's method, aka the Dürüm (or Burrito)
        def rotate(m):
            # transpose + reverse rows == rotate
            m_r = [[r[i] for r in m][::-1] for i in range(len(m[0]))]
            return m_r
        m = [[n**2]]
        for i in range(2*n-2):
            # print(m)
            m.append(list(range(m[-1][0]-1,m[-1][0]-1-len(m[-1]),-1)))
            m = rotate(m)
        return rotate(m)