# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)
        b_count = 0
        penalty = 0
        for i, b in enumerate(boxes):
            result[i] = penalty
            b_count += b == "1"
            penalty += b_count
        penalty = 0
        b_count = 0
        for i in range(len(boxes) - 1, -1, -1):
            result[i] += penalty
            b_count += boxes[i] == "1"
            penalty += b_count
        return result
