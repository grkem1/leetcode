// https://leetcode.com/problems/keys-and-rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set([0])
        target = deque([0])
        while(len(target) != 0):
            t = target.popleft()
            for j in rooms[t]:
                if j not in keys:
                    target.append(j)
                    keys.add(j)
        return(len(keys)==len(rooms))