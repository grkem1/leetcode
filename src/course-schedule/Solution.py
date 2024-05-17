# https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        required_for = [[] for i in range(numCourses)]
        children_count = [0 for i in range(numCourses)]
        seen = [False for i in range(numCourses)]
        for p in prerequisites:
            children_count[p[0]] += 1
            required_for[p[1]].append(p[0])
        reachable = deque()
        for i,c in enumerate(children_count):
            if(c == 0): reachable.append(i)
        # print(reachable)
        while(len(reachable) > 0):
            c = reachable.popleft()
            seen[c] = True
            for h in required_for[c]:
                children_count[h] -= 1
                if(children_count[h] == 0): reachable.append(h)
        # print(seen)
        return(all(seen))