# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        @functools.cache
        def bounded_max_area(i,j): # i,j inclusive
            nonlocal height
            if(i == j): return 0
            # print("i is {}, j is {}, current area is {}".format(i,j,min(height[i],height[j])*(j-i)))
            if(height[i] < height[j]):
                current_area = height[i]*(j-i)
                current_i_height = height[i]
                i += 1
                while(i < j and height[i] < current_i_height):
                    i += 1
                next_area = bounded_max_area(i,j)
                return max(current_area,next_area)
            elif(height[j] < height[i]):
                current_area = height[j]*(j-i)
                current_j_height = height[j]
                j -= 1
                while(i < j and height[j] < current_j_height):
                    j -= 1
                next_area = bounded_max_area(i,j)
                return max(current_area,next_area)
            else:
                current_area = height[i]*(j-i)
                next_area_left = bounded_max_area(i+1,j)
                next_area_right= bounded_max_area(i,j-1)
                return max(current_area,next_area_left,next_area_right)
        return bounded_max_area(0,len(height)-1)