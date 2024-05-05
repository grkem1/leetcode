// https://leetcode.com/problems/design-underground-system

class UndergroundSystem:

    def init_edge(self):
        return [0,0] # total, count


    def __init__(self):
        self.customers = {}
        self.edges = defaultdict(self.init_edge)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.edges[self.customers[id][0]+stationName][0] += (t-self.customers[id][1])
        self.edges[self.customers[id][0]+stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if((startStation+endStation) not in self.edges):return 0
        return self.edges[startStation+endStation][0] / self.edges[startStation+endStation][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)