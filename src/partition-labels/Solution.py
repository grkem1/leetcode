// https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = dict()
        for i,l in enumerate(s):
            if(l in d):
                d[l][1] = i
            else:
                d[l] = [i,i]
        b_e = sorted(d.values())
        ranges = []
        l_r = [-1,-1]
        for r in b_e:
            if(l_r[1] > r[0]):
                l_r[1] = max(l_r[1],r[1])
            else:
                ranges.append(r)
                l_r = r
        return [r[1]-r[0]+1 for r in ranges]