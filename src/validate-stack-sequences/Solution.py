// https://leetcode.com/problems/validate-stack-sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for el in pushed:
            stack.append(el)
            while(len(stack) > 0 and stack[-1] == popped[i]):
                stack.pop()
                i+=1
        return (i == len(popped))