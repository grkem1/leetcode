# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem

# Note that this is not the optimal solution for this problem.
# A better solution can be achieved after the following observations:
# - Sort doesn't need to be on depth of the directory, but simply the length
# - No need for a set, latest added folder is guaranteed to be a parent
#   if there is a parent

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        seen = set()
        folder.sort(key = lambda s: s.count('/'))
        for f in folder:
            found = False
            i = 0
            while((j := f[i+1:].find('/')) != -1):
                if(f[:i+j+1] in seen):
                    found = True
                    break
                # print(f[:i+j+1])
                i += j + 1
            if(not found):
                seen.add(f)
        return list(seen)
