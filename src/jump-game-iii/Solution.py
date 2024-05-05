// https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        reachable = [start]
        seen =  set()
        while(len(reachable) > 0):
            cur = reachable.pop()
            if(arr[cur] == 0): return True
            seen.add(cur)
            if(cur + arr[cur] < len(arr) and (cur+arr[cur]) not in seen):
                reachable.append(cur + arr[cur])
            if(cur - arr[cur] >= 0 and (cur-arr[cur]) not in seen):
                reachable.append(cur - arr[cur])
        return False