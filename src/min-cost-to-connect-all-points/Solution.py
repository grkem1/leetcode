// https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
    def minCostConnectPoints(self, points: [[int]]) -> int:
        # Use Prim's algorithm to span all the given points
        def distance(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        edges = [[] for _ in range(len(points))]
        indices = [0]*len(points)
        for i1,p1 in enumerate(points):
            # ~ for i2 in range(i1+1,len(points)):
            for i2,p2 in enumerate(points):
                if(i1 == i2): continue
                p2 = points[i2]
                d = distance(p1,p2)
                edges[i1].append((d,i2)) # from small to large, don't include twice
        for i in range(len(edges)):
            edges[i].sort()
        # ~ print(edges)
        
        s = {0}
        total_dist = 0
        while(len(s) < len(points)): # while not all points are covered
            # find minimum weight cut. It is guaranteed to be in the MST
            min_dist = 10**7
            min_dist_start = -1
            min_dist_end = -1
            for p1 in s:
                while(indices[p1] < len(edges[p1]) and edges[p1][indices[p1]][1] in s):
                    indices[p1] += 1
                if(indices[p1] < len(edges[p1])):
                    d,p2 = edges[p1][indices[p1]]
                    if(d < min_dist):
                        min_dist = d
                        min_dist_start = p1
                        min_dist_end = p2
            total_dist += min_dist
            s.add(min_dist_end)
            # ~ print(s)
            # ~ print("p1,p2,min_dist: {} {} {}".format(points[min_dist_start],points[min_dist_end],min_dist))
        return total_dist