# https://leetcode.com/problems/remove-duplicate-letters

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = 0
        exists = [0]*len(s)
        positions = collections.defaultdict(lambda : [])
        for i,letter in enumerate(s[::-1]):
            exists[len(s)-1-i] = last | 1 << (ord(letter) - ord('a'))
            last = exists[len(s)-1-i]
            positions[letter].append(len(s)-1-i)
        target = exists[0]
        letters_count = bin(target)[2:].count('1')
        current_s = ""
        current_bitmap = 0
        last_j = -1
        last_position = -1
        while(target != 0):
            #find smallest letter
            smallest_letter = 'a'
            j = 0
            for j in range(last_j+1,26):
                if(target & (1 << j)):
                    smallest_letter = chr(ord('a')+j)
                    break
#            print(smallest_letter)
            last_j = j
            for pos in positions[smallest_letter][::-1]:
                if(pos >= last_position and exists[pos] & target == target):
                    current_s += smallest_letter
                    target ^= (1 << (ord(smallest_letter)-ord('a')))
                    last_j = -1
                    last_position = pos
                    break
#                    target ^= j
        return current_s
