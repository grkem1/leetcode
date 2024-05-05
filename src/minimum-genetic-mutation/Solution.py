// https://leetcode.com/problems/minimum-genetic-mutation

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def dist(s,e):
            ct = 0
            for i in range(len(s)):
                if(s[i] != e[i]):
                    ct += 1
                    if(ct > 1):
                        return 2
            return ct
        count = 0
        q = deque([start,None])
        while(len(q) > 1):
            c = q.popleft()
            if(c == None):
                count += 1
                q.append(None)
                continue
            if(c == end):
                return count
            b_new = []
            for b in bank:
                if(b in q):
                    continue
                d = dist(c,b)
                if(d > 1):
                    b_new.append(b)
                elif(d == 1):
                    q.append(b)
            bank = b_new
        return -1