// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        letter_to_word = dict()
        word_to_letter = dict()
        if(len(pattern) != len(words)):
            return False
        #print(words)
        for index,letter in enumerate(pattern):
            #print(mapping)
            if(letter in letter_to_word or words[index] in word_to_letter):
                if(letter_to_word.get(letter) != words[index] or word_to_letter.get(words[index]) != letter):
                    return False
            else:
                letter_to_word[letter] = words[index]
                word_to_letter[words[index]] = letter
        return True