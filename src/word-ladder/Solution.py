// https://leetcode.com/problems/word-ladder

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        distances = dict((word,-1) for word in wordList)
        if(endWord not in distances):
            return 0
        distances[beginWord] = 0
        words_to_explore = collections.deque()
        words_to_explore.append(beginWord)
        while(len(words_to_explore) > 0):
            word = words_to_explore.popleft()
            for i,l in enumerate(word):
                for new_l in string.ascii_lowercase:
                    neighbor = word[:i] + new_l + word[i+1:]
                    if(neighbor not in distances or distances[neighbor] != -1):
                        continue
                    distances[neighbor] = distances[word]+1
                    # print(neighbor, distances[neighbor])
                    if(neighbor == endWord):
                        return distances[neighbor]+1
                    words_to_explore.append(neighbor)
        return 0