# https://leetcode.com/problems/kth-missing-positive-number

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left,right = 0,len(arr)-1
        if(k < arr[left] - left): return k
        if(k > arr[right] - right - 1): return arr[right] + (len(arr) + k - arr[right])
        while(left < right - 1):
            mid = (left + right) // 2
            if(k < arr[mid] - mid): right = mid
            else: left = mid
        return arr[left] + (left + k - arr[left]) + 1