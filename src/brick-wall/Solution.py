// https://leetcode.com/problems/brick-wall

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = defaultdict(int)
        for row in wall:
            for el in itertools.accumulate(row[:-1]):
                d[el]+=1
        if(len(d)==0): return len(wall)
        return len(wall)-max(d.values())