// https://leetcode.com/problems/minimize-deviation-in-array

class Solution:
    def minimumDeviation(self, nums: [int]) -> int:
        for i in range(len(nums)):
            if(nums[i] %2 == 1):
                nums[i]*=2
        nums.sort()
        all_nums = set()
        def search_base(num,s):
            while(num % 2 == 0):
                num = num//2
                if(num in s):
                    return True
            return False
        nums_compact = []
        for n in nums:
            if(n in all_nums):
                continue
            if(search_base(n,all_nums)):
                continue
            nums_compact.append(-n)
            all_nums.add(-n)
        # print(nums_compact)
        smallest = nums_compact[0]
        heapq.heapify(nums_compact)
        # print(nums_compact)
        deviation = smallest - nums_compact[0]
        while(nums_compact[0]%2==0):
            smallest = max(smallest,nums_compact[0]//2)
            heapq.heapreplace(nums_compact,nums_compact[0]//2)
            # print(smallest)
            deviation = min(deviation,smallest - nums_compact[0])
        return deviation