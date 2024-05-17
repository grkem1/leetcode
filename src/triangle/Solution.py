# https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #convert triangle to its cumulative starting from top
        top = left = right = triangle[0][0]
        for level in triangle[1:]:
            level[0] = left + level[0]
            level[-1] = right + level[-1]
            left = level[0]
            right = level[-1]
        if(len(triangle) > 1):upper_level = triangle[1]
        for level in triangle[2:]:
            for index,number in enumerate(level[1:-1]):
                level[index+1] += min(upper_level[index],upper_level[index+1])
            upper_level = level
        return min(triangle[-1])