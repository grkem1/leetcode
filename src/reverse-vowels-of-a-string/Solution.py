# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        indices = []
        for i,c in enumerate(s):
            if(c in vowels):
                indices.append(i)
        # print(indices)
        for i in range(len(indices)//2):
            s[indices[i]],s[indices[len(indices)-i-1]] = s[indices[len(indices)-i-1]],s[indices[i]]
        return ''.join(s)