# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def convert(row,alternative_row,number):
            count = 0
            for i,t in enumerate(row):
                if(t != number):
                    if(alternative_row[i] == number):
                        count += 1
                    else:
                        return 10**5
            return count
        top_best = min(convert(tops,bottoms,i) for i in range(1,7))
        bottom_best = min(convert(bottoms,tops,i) for i in range(1,7))
        best = min(top_best,bottom_best)
        return best if best < 10**5 else -1