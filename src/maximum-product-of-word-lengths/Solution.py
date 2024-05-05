// https://leetcode.com/problems/maximum-product-of-word-lengths

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=lambda x:len(x),reverse=True)
        def letters_included(w):
            bitmap = 0
            for l in w:
                bitmap |= (1 << (ord(l)-ord('a')))
            return bitmap
        lengths_letters = [(len(w),letters_included(w)) for w in words]
        m = 0
        for index,p in enumerate(lengths_letters[:-1]):
            if(p[0]**2 <= m): return m
            if(p[1] & lengths_letters[index+1][1] == 0):
                return max(m,p[0]*lengths_letters[index+1][0])
            for p2 in lengths_letters[index+1:]:
                if(p[1] & p2[1] == 0):
                    m = max(m,p[0]*p2[0])
        return m