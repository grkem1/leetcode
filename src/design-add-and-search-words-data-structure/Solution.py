# https://leetcode.com/problems/design-add-and-search-words-data-structure

class WordDictionary:

    def __init__(self):
        self.trie = dict()
        

    def addWord(self, word: str) -> None:
        current = self.trie
        for letter in word:
            if(letter not in current):
                current[letter] = dict()
            current = current[letter]
        current['#'] = '#'

    def search(self, word: str, t = None) -> bool:
        if(t == None):
            t = self.trie
        current = t
        for index,letter in enumerate(word):
            if(letter not in current):
                if(letter == '.'):
                    return any(self.search(l+word[index+1:], current) for l in current if l != '#')
                else:
                    return False
            current = current[letter]
        if('#' in current):
            return True
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)