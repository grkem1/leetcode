// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words = collections.Counter(words)
        middle = False
        c = 0
        for w in words:
            if(w[0] == w[1]):
                c += (words[w]//2)*4
                if(not middle and words[w]%2 == 1):
                    middle = True
                    c += 2
            elif(w[::-1] in words):
                c += 2*min(words[w],words[w[::-1]])
        return c