# https://leetcode.com/problems/find-center-of-star-graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if(edges[0][0] == edges[1][0]):
            return edges[0][0]
        elif(edges[0][0] == edges[1][1]):
            return edges[0][0]
        return edges[0][1]
        # return set(edges[0]).intersection(set(edges[1])).pop()
