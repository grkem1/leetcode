# https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = Counter(sorted(candidates))
        candidates_list = list(candidates)
        results = []
        current_result = []
        def dfs(i,t):
            nonlocal results, current_result, candidates_list
            if(t == 0):
                results.append(current_result.copy())
                return
            if(i > len(candidates_list)-1 or candidates_list[i] > t):
                return
            if(candidates[candidates_list[i]] > 0):
                candidates[candidates_list[i]] -= 1
                current_result.append(candidates_list[i])
                dfs(i,t-candidates_list[i])
                current_result.pop()
                candidates[candidates_list[i]] += 1
            dfs(i+1,t)
        dfs(0,target)
        return results
