# https://leetcode.com/problems/arithmetic-subarrays

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check_valid(left,right):
            nonlocal nums
            array = list(sorted(nums[left:right+1]))
            step = array[1] - array[0]
            last = array[1]
            # print(array)
            for el in array[2:]:
                if(el - last != step):
                    return False
                last = el
            return True
        rv = []
        for i,left in enumerate(l):
            right = r[i]
            # print(left,right)
            rv.append(check_valid(left,right))
        return rv