// https://leetcode.com/problems/find-and-replace-pattern

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # works with Python 3.7
        def find_id(input):
            id = dict()
            for index,letter in enumerate(input):
                if(letter in id):
                    id[letter].append(index)
                else:
                    id[letter] = [index]
            return id
        def compare_ids(id1,id2):
            if(len(id1) != len(id2)): return False
            return(all(a == b for a,b in zip(id1,id2)))
        return [w for w in words if ( compare_ids(find_id(pattern).values(),find_id(w).values()) )]