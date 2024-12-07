# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def isPossible(bag):
            nonlocal nums, maxOperations
            total = 0
            for n in nums:
                total += math.ceil(n / bag) - 1
                if total > maxOperations:
                    return False
            return True

        low = 1
        high = max(nums)
        while low + 1 < high:
            mid = (low + high) // 2
            if isPossible(mid):
                high = mid
            else:
                low = mid
        # print(low, mid, high)
        return high
