# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        queries = sorted(
            [sorted(q) + [i] for i, q in enumerate(queries)],
            key=lambda k: k[1],
            reverse=True,
        )
        stack = []
        last = len(heights)
        output = [-1] * len(queries)
        for q in queries:
            if q[0] == q[1] or heights[q[1]] > heights[q[0]]:
                output[q[2]] = q[1]
                continue
            for i in range(last - 1, q[1], -1):
                while stack and stack[-1][0] < heights[i]:
                    stack.pop()
                stack.append([heights[i], i])
            last = q[1] + 1
            i = bisect.bisect_left(stack, -heights[q[0]], key=lambda x: -x[0])
            # print(q,i,stack)
            if -1 < i - 1 < len(stack):
                output[q[2]] = stack[i - 1][1]
        return output
