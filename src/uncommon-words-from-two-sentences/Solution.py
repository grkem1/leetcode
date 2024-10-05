# https://leetcode.com/problems/uncommon-words-from-two-sentences

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1 = s1.split()
        s2 = s2.split()
        s1_ctr = Counter(s1)
        s2_ctr = Counter(s2)
        uncommon = []
        for w in s1:
            if s1_ctr[w] == 1 and w not in s2_ctr:
                uncommon.append(w)
        for w in s2:
            if s2_ctr[w] == 1 and w not in s1_ctr:
                uncommon.append(w)
        return uncommon
