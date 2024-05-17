# https://leetcode.com/problems/short-encoding-of-words

class Solution:
    def minimumLengthEncoding(self,words:[str])->int:
        if(len(words) == 0): return 0
        if(len(words) == 1): return len(words[0])+1
        words.sort(key = lambda w: len(w))
        length = len(words[-1])+1
        uniqueIndicator = [True]*len(words)
        for i in range(len(words)-2,-1,-1):
            for j in range(i+1,len(words)):
                if(not uniqueIndicator[j]):
                    continue
                if(words[j][-len(words[i]):] == words[i]):
                    uniqueIndicator[i] = False
                    break
            if(uniqueIndicator[i]): length += len(words[i])+1
        return length