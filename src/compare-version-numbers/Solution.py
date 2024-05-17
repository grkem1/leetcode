# https://leetcode.com/problems/compare-version-numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        if(len(v1) > len(v2)):
            v2 = v2 + [0]* (len(v1) - len(v2))
        else:
            v1 = v1 + [0]* (len(v2) - len(v1))
        # print(v1)
        # print(v2)
        for p in zip(v1,v2):
            if(p[0] > p[1]):
                return 1
            elif(p[1] > p[0]):
                return -1
        return 0