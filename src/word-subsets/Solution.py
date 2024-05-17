# https://leetcode.com/problems/word-subsets

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w2_uni_threshold = collections.Counter(words2[0])
        for w in words2[1:]:
            w_ctr = collections.Counter(w)
            for l in set(w2_uni_threshold+w_ctr):
                w2_uni_threshold[l] = max(w2_uni_threshold[l],w_ctr[l])
        def includes(w:str):
            nonlocal w2_uni_threshold
            w_ctr = collections.Counter(w)
            for l in w2_uni_threshold:
                if(w_ctr[l] < w2_uni_threshold[l]):
                    return False
            return True
        return filter(includes,words1)
        