// https://leetcode.com/problems/minimum-absolute-difference

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mins = []
        mins_diff = 2*10**6
        smaller = arr[0]
        for bigger in arr[1:]:
            if(bigger-smaller < mins_diff):
                mins_diff = bigger-smaller
                mins = [[smaller,bigger]]
            elif(bigger-smaller == mins_diff):
                mins.append([smaller,bigger])
            smaller = bigger
        return mins