# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        s = [l for l in s]
        locked = [l for l in locked]
        free = deque()
        level = 0
        for i, l in enumerate(s):
            if locked[i] == "0":
                free.append(i)
                continue
            if l == "(":
                level += 1
            else:
                level -= 1
                if level < 0:
                    if len(free) > 0:
                        j = free.popleft()
                        locked[j] = "1"
                        s[j] = "("
                        level += 1
                    else:
                        return False
        if level == 0:
            return True
        level = 0
        free = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == "0":
                free += 1
            elif s[i] == ")":
                level += 1
            else:
                level -= 1
                if level < 0:
                    if free > 0:
                        free -= 1
                        level += 1
                    else:
                        return False
        return level == 0
