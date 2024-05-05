// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solns_array = []
        candidates.sort()
        def recurse_down(candidates,target,current):
            nonlocal solns_array
            if(target == 0):
                solns_array.append(current)
            if(candidates[0] > target):
                return
            for i in range(len(candidates)):
                if(len(current) > 0 and candidates[i] < current[-1]):
                    continue
                recurse_down(candidates,target-candidates[i],current+[candidates[i]])
        recurse_down(candidates,target,[])
        return solns_array