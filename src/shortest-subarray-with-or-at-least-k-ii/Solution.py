# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if(len(nums) == -1):
            return -1
        if(k == 0):
            return 1
        def add_freq(num, f, acc):
            i = 0
            while(2 ** i <= num):
                if(num & 2**i):
                    f[i] += 1
                i += 1
            return acc | num
        def remove_freq(num, f, acc):
            i = 0
            while(2 ** i <= num):
                if(num & 2**i):
                    f[i] -= 1
                    if(f[i] == 0):
                        acc &= ~2**i
                i += 1
            return acc
        i = 0
        j = -1
        best = len(nums) + 1
        freq = [0]*32
        acc = 0
        acc = add_freq(nums[0], freq, acc)
        while(i < len(nums)):
            # print(i,j, best, acc, freq)
            if(acc < k):
                i += 1
                if(i >= len(nums)): break
                acc = add_freq(nums[i], freq, acc)
            else:
                best = min(best, i - j)
                j += 1
                acc = remove_freq(nums[j], freq, acc)
        # print(best)
        return best if best <= len(nums) else -1
