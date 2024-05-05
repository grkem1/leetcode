// https://leetcode.com/problems/sort-vowels-in-a-string

class Solution:
    def sortVowels(self, s: str) -> str:
        t = list(s)
        s_wovels = []
        s_wovels_i = []
        wovels = {'a','e','i','o','u','A','E','I','O','U'}
        for i,l in enumerate(s):
            if(l in wovels):
                s_wovels.append(l)
                s_wovels_i.append(i)
        s_wovels.sort()
        for i_w in zip(s_wovels_i,s_wovels):
            t[i_w[0]] = i_w[1]
        return ''.join(t)