// https://leetcode.com/problems/buddy-strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)): return False
        letters = []
        seen = set()
        repeating = False
        for i,(a,b) in enumerate(zip(s,goal)):
            # print(a,b)
            if(a in seen):
                repeating = True
            seen.add(a)
            if(a != b):
                letters.append(i)
                if(len(letters) > 2): return False
        # print(letters)
        return len(letters) == 2 and s[letters[0]] == goal[letters[1]] and goal[letters[0]] == s[letters[1]] or repeating and len(letters) == 0