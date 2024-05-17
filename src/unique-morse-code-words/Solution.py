# https://leetcode.com/problems/unique-morse-code-words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformation = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in words:
            seen.add("".join( (transformation[ord(l)-ord('a')] for l in word ) ))
        # print(seen)
        return len(seen)