# https://leetcode.com/problems/4sum-ii

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        def twoSum(n1,n2,target):
            count = 0
            i = 0
            j = len(n2)-1
            while(i < len(n1) and j >= 0):
                # print(i,n1[i])
                # print(j,n2[j])
                s = n1[i]+n2[j]
                if(s > target):
                    j-=1
                elif(s < target):
                    i+=1
                else:
                    i+=1
                    j-=1
                    i_count = 1
                    j_count = 1
                    while(i < len(n1) and n1[i] == n1[i-1]):
                        i_count+=1
                        i+=1
                    while(j >= 0 and n2[j] == n2[j+1]):
                        j_count+=1
                        j-=1
                    count += i_count*j_count
            return count
        targets = collections.defaultdict(int)
        for el3 in nums3:
            for el4 in nums4:
                targets[-(el3+el4)] += 1
        
        # a = sorted([1,2,3,4,5])
        # b = sorted([-1,-2,-3,-4,-5])
        # print(twoSum(a,b,0))
        
        total_count = 0
        for t in targets:
            if(targets[t] != 0):
                # print(t,targets[t],twoSum(nums1,nums2,t))
                total_count += targets[t]*twoSum(nums1,nums2,t)
                targets[t] = 0
        return total_count