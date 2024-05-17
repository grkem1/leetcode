# https://leetcode.com/problems/valid-mountain-array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr)<3):return False
        increasing = True
        for i in range(1,len(arr)):
            if(increasing):
                if(arr[i] < arr[i-1]):
                    if(i == 1): return False
                    increasing = False
                elif(arr[i] == arr[i-1]):
                    return False
            else:
                if(arr[i] >= arr[i-1]):
                    return False
        return (increasing == False)