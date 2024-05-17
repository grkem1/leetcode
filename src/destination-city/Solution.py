# https://leetcode.com/problems/destination-city

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = dict()
        for p in paths:
            if(p[1] not in cities):
                cities[p[1]] = False
            cities[p[0]] = True
        for c in cities:
            if(cities[c] == False):
                return c