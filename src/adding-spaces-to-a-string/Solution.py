# https://leetcode.com/problems/adding-spaces-to-a-string


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(-1)
        next_space = 0
        result = []
        for i, s in enumerate(s):
            if i == spaces[next_space]:
                next_space += 1
                result.append(" ")
            result.append(s)
        return "".join(result)
