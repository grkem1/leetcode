# https://leetcode.com/problems/find-missing-observations

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = ( len(rolls) + n ) * mean
        remaining = total - sum(rolls)
        remaining_mean = remaining / n
        if(remaining_mean > 6 or remaining_mean < 1):
            return []
        remaining_mean = math.floor(remaining_mean)
        extra = remaining - remaining_mean * n
        return [remaining_mean] * (n-extra) + [remaining_mean + 1] * extra
