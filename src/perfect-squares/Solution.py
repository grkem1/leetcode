// https://leetcode.com/problems/perfect-squares

class Solution:
    def numSquares(self, n: int) -> int:
        seen = set([n])
        level = 1
        level_queue = deque([n, None])
        for _ in range(10000):
            number = level_queue.popleft()
            if(number == None):
                level += 1
                level_queue.append(None)
                continue
            for i in range(1,int((number)**(1/2))+1):
                new_number = number - i**2
                if(new_number in seen or new_number < 0):
                    continue
                if(new_number == 0):
                    return level
                level_queue.append(new_number)
                seen.add(new_number)
                # print(seen)
                # print(level_queue)