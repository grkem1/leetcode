# https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        candidates = []
        seen_once = dict()
        seen_twice = set()
        for i in range(len(s)-1,-1,-1):
            l = s[i]
            if(l in seen_once):
                seen_twice.add(l)
            else:
                seen_once[l] = i
                candidates.append(l)
        # print(candidates)
        # print(seen_once)
        # print(seen_twice)
        while(len(candidates) > 0):
            l = candidates.pop()
            if(l not in seen_twice):
                return seen_once[l]
        return -1