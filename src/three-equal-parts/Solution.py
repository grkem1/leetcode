# https://leetcode.com/problems/three-equal-parts

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        one_count = arr.count(1)
        if(one_count % 3 != 0): return [-1,-1]
        if(one_count == 0): return[0,2]
        one_indices = [0,0,0,0,0]
        c = 0
        first_one=0
        for i,b in enumerate(arr):
            if(b == 0):continue
            c+=1
            if(c == 1):first_one=i
            if(c == one_count//3):one_indices[0]=i
            if(c == one_count//3+1):one_indices[1]=i
            if(c == (one_count//3)*2):one_indices[2]=i
            if(c == (one_count//3)*2+1):one_indices[3]=i
            if(c == one_count):
                one_indices[-1]=i
                break
        ending_zeros = len(arr)-one_indices[-1]-1
        if(one_indices[0]+ending_zeros>=one_indices[1] or one_indices[2]+ending_zeros>=one_indices[3]):
            return [-1,-1]
        # print(one_indices)
        if(not (arr[first_one:one_indices[0]+1]==arr[one_indices[1]:one_indices[2]+1]==arr[one_indices[3]:one_indices[4]+1])):
            return [-1,-1]
        # print(one_indices)
        return [one_indices[0]+ending_zeros,one_indices[2]+ending_zeros+1]