// https://leetcode.com/problems/implement-trie-prefix-tree

class Trie:

    def __init__(self):
        self.t = {}


    def insert(self, word: str) -> None:
        d = self.t
        for i in range(len(word)):
            if(word[i] not in d): 
                d[word[i]] = [False,{}]
            if(i == len(word)-1):d[word[i]][0] = True
            d = d[word[i]][1]

    def search(self, word: str) -> bool:
        d = self.t
        for i in range(len(word)):
            if(word[i] not in d): 
                return False
            if(i == len(word)-1):
                return d[word[i]][0]
            d = d[word[i]][1]


    def startsWith(self, prefix: str) -> bool:
        d = self.t
        for i in range(len(prefix)):
            if(prefix[i] not in d): 
                return False
            d = d[prefix[i]][1]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)