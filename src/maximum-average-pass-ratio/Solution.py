# https://leetcode.com/problems/maximum-average-pass-ratio


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def diff(x, y):
            return (x - y) / (x * (x + 1))

        classes = [[-diff(c[1], c[0]), c[1], c[0]] for c in classes]
        heapq.heapify(classes)
        for _ in range(extraStudents):
            if classes[0][1] == classes[0][2]:
                break
            heapq.heapreplace(
                classes,
                [
                    -diff(classes[0][1] + 1, classes[0][2] + 1),
                    classes[0][1] + 1,
                    classes[0][2] + 1,
                ],
            )
            # print(classes)
        return sum(c[2] / c[1] for c in classes) / len(classes)
