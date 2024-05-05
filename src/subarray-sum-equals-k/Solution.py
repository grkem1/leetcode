// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sums = list(itertools.accumulate(nums)) + [0]
        # i,j = 0,0
        # counter = 0
        # while(j < len(nums)):
        #     curr_sum = sums[j] - sums[i-1]
        #     if(curr_sum < k):
        #         j += 1
        #     elif(curr_sum > k):
        #         i += 1
        #         if(i > j):
        #             j += 1
        #     else:
        #         # print(i,j)
        #         counter += 1
        #         j += 1
        # return counter
        sums = collections.defaultdict(int)
        sums[0] = 1
        cum = 0
        count = 0
        for n in nums:
            # print(sums)
            cum += n
            count += sums.get(cum - k,0)
            sums[cum]+=1
        return count