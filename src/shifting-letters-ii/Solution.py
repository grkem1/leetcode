# https://leetcode.com/problems/shifting-letters-ii


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        result = []
        backward_forward = [[], []]
        for shift in shifts:
            heapq.heappush(backward_forward[shift[-1]], shift[0])
            heapq.heappush(backward_forward[1 - shift[-1]], shift[1] + 1)
        current = 0
        for i, l in enumerate(s):
            while len(backward_forward[1]) > 0 and backward_forward[1][0] == i:
                current += 1
                heapq.heappop(backward_forward[1])
            while len(backward_forward[0]) > 0 and backward_forward[0][0] == i:
                current -= 1
                heapq.heappop(backward_forward[0])
            result.append(chr((ord(l) - ord("a") + current) % 26 + ord("a")))
        return "".join(result)
