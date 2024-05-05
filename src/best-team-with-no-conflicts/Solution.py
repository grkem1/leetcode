// https://leetcode.com/problems/best-team-with-no-conflicts

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages,scores))
        best = 0
        top_max = defaultdict(int)
        top_max[0] = 0
        for p in players:
            candidates = []
            for top in top_max:
                if(top <= p[1]):
                    candidates.append(top)
            for c in candidates:
                top_max[p[1]] = max(top_max[p[1]], top_max[c]+p[1])
                best = max(best, top_max[p[1]])
        return best