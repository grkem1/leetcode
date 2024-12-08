# https://leetcode.com/problems/two-best-non-overlapping-events


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        best_after = [0] * len(events)
        best = 0
        for i, e in enumerate(events[::-1]):
            best = max(best, e[2])
            best_after[-i - 1] = [e[0], best]
        best = 0
        for i, e in enumerate(events):
            non_overlapping = bisect.bisect_right(best_after, [e[1], 10**9])
            if non_overlapping < len(best_after):
                best = max(best, best_after[non_overlapping][1] + e[2])
            else:
                best = max(best, e[2])
        # print(best_after)
        return best
