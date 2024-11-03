# https://leetcode.com/problems/defuse-the-bomb

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if(k == 0): return [0] * len(code)
        if(k > 0):
            left = 1
            right = k
            current = sum(code[left:right + 1])
        if(k < 0):
            left = k
            right = -1
            current = sum(code[left:])
        result = [current]
        for i in range(len(code) - 1):
            current -= code[left]
            left = (left + 1 ) % len(code)
            right = (right + 1) % len(code)
            current += code[right]
            result.append(current)
        return result
