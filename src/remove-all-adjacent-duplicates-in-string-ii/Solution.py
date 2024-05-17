# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        for c in s:
            if(len(stack) > 0 and stack[-1][0] == c):
                stack[-1][1] += 1
                if(stack[-1][1] == k):
                    stack.pop()
            else:
                stack.append([c,1])
        return "".join([i[1]*i[0] for i in stack])