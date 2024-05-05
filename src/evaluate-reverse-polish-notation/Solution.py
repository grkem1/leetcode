// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def div(a,b):
            if((a < 0) ^ (b < 0)): return -(-b//a)
            else: return (b//a)
        operands_stack = deque()
        for t in tokens:
            if(t == '+'):
                operands_stack.append(operands_stack.pop() + operands_stack.pop())
            elif(t == '-'):
                operands_stack.append(- (operands_stack.pop() - operands_stack.pop()))
            elif(t == '*'):
                operands_stack.append(operands_stack.pop() * operands_stack.pop())
            elif(t == '/'):
                operands_stack.append(div(operands_stack.pop(),operands_stack.pop()))
            else:
                operands_stack.append(int(t))
        return operands_stack[-1]