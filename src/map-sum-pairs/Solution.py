# https://leetcode.com/problems/map-sum-pairs

class MapSum:
    def __init__(self):
        self.d = dict()
        self.inserted = dict()

    def insert(self, key: str, val: int) -> None:
        if(key in self.inserted):
            diff = val - self.inserted[key]
            if(diff == 0):return
            self.inserted[key],val = val,diff
        else:
            self.inserted[key]=val
        d = self.d
        for k in key:
            if(k in d): 
                d[k][0]+=val
            else:
                d[k] = [val,dict()]
            d = d[k][1]

    def sum(self, prefix: str) -> int:
        d = self.d
        val = 0
        for p in prefix:
            if(p in d):
                val = d[p][0]
                d = d[p][1]
            else:
                return 0
        return val



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)