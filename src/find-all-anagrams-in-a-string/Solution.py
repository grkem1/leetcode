# https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(p) > len(s)):
            return []
        anagrams = []
        window,pattern = collections.Counter(s[:len(p)]),collections.Counter(p)
        # diff = dict((k,pattern[k]-window.get(k,0)) for k in pattern)
        diff = collections.defaultdict(int)
        for l in pattern:
            d = pattern[l] - window[l]
            if(d != 0):
                diff[l] = d
        i = 0
        if(len(diff) == 0):
            anagrams.append(i)
        i+=1
        # print(diff)
        while(i + len(p) <= len(s)):
            if(s[i+len(p)-1] in pattern):
                diff[s[i + len(p) - 1]]-=1
                if(diff[s[i+len(p)-1]] == 0):
                    del(diff[s[i+len(p)-1]])
            if(s[i-1] in pattern):
                diff[s[i-1]]+=1
                if(diff[s[i-1]]==0):
                    del(diff[s[i-1]])
            # print(diff)

            if(len(diff)==0):
                anagrams.append(i)
            i+=1
            # print(i,len(p),len(s))
        # print(anagrams)
        return anagrams